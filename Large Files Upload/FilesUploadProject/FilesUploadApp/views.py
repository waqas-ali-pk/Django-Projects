import datetime
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import FileUploadCreateForm
from django.http import HttpResponse, JsonResponse


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


class AjaxResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class FileUploadSecondCreate(AjaxResponseMixin, CreateView):

    template_name = 'file_upload_form_2.html'
    form_class = FileUploadCreateForm

    def form_valid(self, form):
        print(form)
        print(form.instance.file)
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = 0

        form.save()
        return super(FileUploadSecondCreate, self).form_valid(form)

