from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello_world),
    url(r'^del_info_api', views.del_info_api),
    url(r'^get_info_api', views.get_info_api),
    url(r'^put_info_api', views.put_info_api)
]