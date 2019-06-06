from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [

    url(r'file_upload/$', views.FileUploadCreate.as_view(), name='file_upload'),

]
