from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views
from .views import file_upload_second_success_url

urlpatterns = [

    url(r'file_upload/$', views.FileUploadCreate.as_view(), name='file_upload'),
    url(r'file_upload_2/$', views.FileUploadSecondCreate.as_view(), name='file_upload_2'),
    url(r'file_upload_second_success_url/$', file_upload_second_success_url, name='file_upload_second_success_url'),

]
