import datetime
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import FileUploadCreateForm
from django.http import HttpResponse
# Create your views here.


class FileUploadCreate(CreateView):

    template_name = 'file_upload_form.html'
    form_class = FileUploadCreateForm

    def form_valid(self, form):
        print(form)
        print(form.instance.file)
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = 0

        file_upload = form.save()
        file_upload.save()

        return HttpResponse("File uploaded successfully")


def file_upload_second_success_url(request):
    return HttpResponse("File uploaded successfully")


class FileUploadSecondCreate(CreateView):

    template_name = 'file_upload_form_2.html'
    form_class = FileUploadCreateForm

    def form_valid(self, form):
        print(form)
        print(form.instance.file)
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = 0

        form.save()
        return super(FileUploadSecondCreate, self).form_valid(form)

