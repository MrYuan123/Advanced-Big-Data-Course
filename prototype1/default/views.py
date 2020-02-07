from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotModified
import json
from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError
from . import dao
from . import models
import uuid


@csrf_exempt
def del_info_api(request):
    if request.method == "GET":
        return render(request, 'access-api.html', locals())
    else:
        json_data = {}
        try:
            json_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"Error": "Json Missing!"}, status=400)

        try:
            models.UserJSON(**json_data)
        except ValidationError as e:
            return JsonResponse({"Error": e.errors()}, status=400)

        try:
            name = json_data["name"]
            user_info = dao.dao().delfun(name)
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        dao.dao().clearETagfun()
        return JsonResponse({'Delete': 'Success'})


@csrf_exempt
def get_info_api(request):
    if request.method == "GET":
        return render(request, 'access-api.html', locals())
    else:
        json_data = {}
        try:
            json_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"Error": "Json Missing!"}, status=400)

        try:
            models.UserJSON(**json_data)
        except ValidationError as e:
            return JsonResponse({"Error": e.errors()}, status=400)

        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        try:
            user_info = dao.dao().getfunc(json_data['name'])
            if len(user_info) != 0:
                user_info['name'] = json_data['name']
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        response = JsonResponse(user_info)
        response["ETag"] = etag

        return response


@csrf_exempt
def put_info_api(request):
    if request.method == "GET":
        return render(request, 'access-api.html', locals())
    else:
        json_data = {}
        try:
            json_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"Error": "Json Missing!"}, status=400)

        try:
            models.InfoJSON(**json_data)
        except ValidationError as e:
            return JsonResponse({"Error": e.errors()}, status=400)

        try:
            name = json_data["name"]
            del json_data['name']
            user_info = dao.dao().setfunc(name, json_data)
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        dao.dao().clearETagfun()
        return JsonResponse({'Put': 'Success'})


def hello_world(request):
    return render(request, 'hello-world.html', locals())

