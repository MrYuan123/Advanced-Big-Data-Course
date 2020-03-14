from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotModified
import json
from django.views.decorators.csrf import csrf_exempt
from . import dao
from . import validator
import uuid
from jsonschema import validate



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

        # try:
        #     models.UserJSON(**json_data)
        # except ValidationError as e:
        #     return JsonResponse({"Error": e.errors()}, status=400)

        try:
            objectId = json_data["objectId"]
            user_info = dao.dao().deljsonfunc(objectId)
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

        # try:
        #     models.UserJSON(**json_data)
        # except ValidationError as e:
        #     return JsonResponse({"Error": e.errors()}, status=400)

        if 'If-None-Match' in request.headers:
            if dao.dao().getETagfun(request.headers['If-None-Match']) is not False:
                response = HttpResponseNotModified()
                response['ETag'] = request.headers['If-None-Match']
                return response

        try:
            print(json_data['objectId'])
            json_info = dao.dao().getjsonfunc(json_data['objectId'])
            print(json_info)
        except Exception as e:
            print(e)
            return HttpResponse("Database Error!", status=500)

        etag = uuid.uuid4().hex
        dao.dao().setETagfun(etag)
        if json_info is None:
            return JsonResponse({})

        response = JsonResponse(json.loads(json_info.decode('utf-8')))
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
            return JsonResponse({"Error": "Wrong Json!"}, status=400)

        try:
            validate(json_data, validator.json_schema)
        except Exception as error:
            print(error)
            return JsonResponse({"Schema Error": str(error)})

        try:
            user_info = dao.dao().setjsonfunc(json_data['objectId'], json.dumps(json_data))
        except Exception as e:
            return HttpResponse("Database Error!", status=500)

        # print(json_data)
        # print(validator.json)
        # try:
        #     jsonschema.validate(json, validator.json_schema)
        # except Exception as error:
        #     print(error.message)
        # else:
        #     return JsonResponse({'Putttttttt': 'Success'})
        #
        # return JsonResponse({'Put': 'Success'})
        #
        # try:
        #     models.InfoJSON(**json_data)
        # except ValidationError as e:
        #     return JsonResponse({"Error": e.errors()}, status=400)
        #
        # try:
        #     name = json_data["name"]
        #     del json_data['name']
        #     user_info = dao.dao().setfunc(name, json_data)
        # except Exception as e:
        #     return HttpResponse("Database Error!", status=500)

        dao.dao().clearETagfun()
        return JsonResponse({'Put': 'Success'})


def hello_world(request):
    return render(request, 'hello-world.html', locals())

