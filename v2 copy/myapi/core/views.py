from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse, HttpResponseNotModified
from . import dao, validator, parsedata, models
import json, uuid, ast
from jsonschema import validate
from elasticsearch import Elasticsearch
es = Elasticsearch()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        dict = validator.json_content
        out = parsedata.modification(dict, '12xvxc345ssdsds-508', 'creationDate', "01-01-2020")
        return Response(out)


class DemoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        objectid = request.GET["objectid"]
        json_info = dao.dao().getjsonfunc("data")
        if json_info is None:
            result = {}
        else:
            info = json.loads(json_info.decode('utf-8'))
            result = parsedata.findDict(info, objectid)
            # result = json.loads(json_info.decode('utf-8'))

        response = JsonResponse({"result": result})

        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag
        return response

        # content = {'message': objectid}
        # return Response(content)

    def delete(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        objectid = request.GET["objectid"]
        try:
            result = addQueue("delete", None)
        except:
            pass

        try:
            user_info = dao.dao().deljsonfunc("data")
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        dao.dao().clearETagfun()
        es_op = {}
        try:
            es_op = es.delete(index="data", doc_type="doc", id=1)
        except:
            pass

        return JsonResponse({'Delete': 'Success', "es_op": es_op})

    def put(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        json_data = {}
        json_data = json.loads(request.body)
        try:
            result = addQueue("create", json_data)
        except:
            pass


        try:
            validate(json_data, validator.json_schema)
        except Exception as error:
            print(error)
            return JsonResponse({"Schema Error": str(error)})

        dao.dao().setjsonfunc("data", json.dumps(json_data))


        es_op = {}
        try:
            es_op = es.index(index="data", doc_type="doc", id=1, body=json_data)
        except:
            pass

        # output = parsedata.parser(json_data)
        #
        # for item in output:
        #     user_info = dao.dao().setjsonfunc(item['objectId'], json.dumps(item))

        dao.dao().clearETagfun()

        response = JsonResponse({'put': "success", "es_op": es_op})
        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag
        return response

    def patch(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        objectid = request.GET['objectid']
        data = dao.dao().getjsonfunc("data")
        if data is None:
            return JsonResponse({"result" : "empty"})


        datadict = json.loads(data.decode('utf-8'))

        try:
            result = addQueue("create", datadict)
        except:
            pass


        for item in request.GET:
            if item is not "objectid":
                value = request.GET[item]
                if item == "deductible" or item == "copay":
                    value = int(value)
                datadict = parsedata.modification(datadict, objectid, item, value)

        dao.dao().setjsonfunc("data", json.dumps(datadict))

        es_op = {}
        try:
            es_op = es.index(index="data", doc_type="doc", id=1, body=datadict)
        except:
            pass

        dao.dao().clearETagfun()

        response = JsonResponse({'patch': "success", "es_op": es_op})
        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag
        return response


        # data = dao.dao().getjsonfunc(objectid)
        # str = data.decode("UTF-8")
        # data = ast.literal_eval(str)
        #
        # for item in request.GET:
        #     data[item] = request.GET[item]
        #
        # dao.dao().setjsonfunc(objectid, json.dumps(data))



        # for item in json_data:
        #     data[item] = json_data[item]
        #
        # dao.dao().setjsonfunc(objectid, data)
        #
        # dao.dao().clearETagfun()
        #
        # response = JsonResponse({'patch': "success"})
        # etag = uuid.uuid4().hex
        # dao.dao().setETagfun(etag)
        # response["ETag"] = etag
        # return response


class ElasticSearchView(APIView):
    def post(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        content = json.loads(request.body)
        result = {}
        try:
            result = es.search(index="data", body=content)
        except:
            pass

        response = JsonResponse(result)
        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag

        return response


from redis import Redis
from rq import Queue
q = Queue(connection=Redis(host='127.0.0.1', port='6379'))
# host='127.0.0.1', port='6379'

def addQueue(task_type, body):
    if task_type == "create":
        result = q.enqueue(es.index, {"index":"data", "doc_type": "doc", "id": 1, "body": body})
    if task_type == "delete":
        result = q.enqueue(es.delete, {"index":"data", "doc_type":"doc", "id":1})

    return result


