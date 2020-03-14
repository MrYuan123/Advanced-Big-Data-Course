from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse, HttpResponseNotModified
from . import dao, validator, parsedata
import json, uuid, ast
from jsonschema import validate


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class DemoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        objectid = request.GET["objectid"]
        print(objectid)
        json_info = dao.dao().getjsonfunc(objectid)
        if json_info is None:
            result = {}
        else:
            result = json.loads(json_info.decode('utf-8'))

        response = JsonResponse({"result": result})

        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag
        return response

        # content = {'message': objectid}
        # return Response(content)

    def delete(self, request):
        objectid = request.GET["objectid"]

        try:
            user_info = dao.dao().deljsonfunc(objectid)
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        dao.dao().clearETagfun()
        return JsonResponse({'Delete': 'Success'})

    def put(self, request):
        json_data = {}
        json_data = json.loads(request.body)

        try:
            validate(json_data, validator.json_schema)
        except Exception as error:
            print(error)
            return JsonResponse({"Schema Error": str(error)})

        output = parsedata.parser(json_data)

        for item in output:
            user_info = dao.dao().setjsonfunc(item['objectId'], json.dumps(item))

        dao.dao().clearETagfun()

        response = JsonResponse({'put': "success"})
        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag
        return response

    def patch(self, request):
        objectid = request.GET['objectid']

        data = dao.dao().getjsonfunc(objectid)
        str = data.decode("UTF-8")
        data = ast.literal_eval(str)

        for item in request.GET:
            data[item] = request.GET[item]

        dao.dao().setjsonfunc(objectid, json.dumps(data))

        dao.dao().clearETagfun()

        response = JsonResponse({'patch': "success"})
        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response["ETag"] = etag
        return response
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


