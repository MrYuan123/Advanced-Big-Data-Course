from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse, HttpResponseNotModified
from . import dao, validator, parsedata, models
import json, uuid, ast
from jsonschema import validate
from django.core import serializers


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        dict = validator.json_content
        out = parsedata.modification(dict, '12xvxc345ssdsds-508', 'creationDate', "01-01-2020")
        # obj = models.planCostShares(**validator.json_content["planCostShares"])
        # content = {"result" : obj.objectId}
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
            user_info = dao.dao().deljsonfunc("data")
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        dao.dao().clearETagfun()
        return JsonResponse({'Delete': 'Success'})

    def put(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        json_data = {}
        json_data = json.loads(request.body)

        try:
            validate(json_data, validator.json_schema)
        except Exception as error:
            print(error)
            return JsonResponse({"Schema Error": str(error)})

        dao.dao().setjsonfunc("data", json.dumps(json_data))
        # output = parsedata.parser(json_data)
        #
        # for item in output:
        #     user_info = dao.dao().setjsonfunc(item['objectId'], json.dumps(item))

        dao.dao().clearETagfun()

        response = JsonResponse({'put': "success"})
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
        for item in request.GET:
            if item is not "objectid":
                value = request.GET[item]
                print(item)
                if item == "deductible" or item  == "copay":
                    value = int(value)
                print(type(value))
                datadict = parsedata.modification(datadict, objectid, item, value)

        dao.dao().setjsonfunc("data", json.dumps(datadict))

        dao.dao().clearETagfun()

        response = JsonResponse({'patch': "success"})
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


