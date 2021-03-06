import datetime
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import FileUploadCreateForm
from django.http import HttpResponse, JsonResponse
import csv
from django.conf import settings


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


def make_and_download_csv(request):

    lst = [[1, 2, 3], [1, 2, 3]]
    random_str = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S%f")
    csv_dir = str(settings.BASE_DIR) + "/CSV Files/"
    csv_name = "csv_" + str(random_str)
    ext = "csv"
    csv_path = csv_dir + csv_name + "." + ext
    with open(csv_path, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(lst)
    writeFile.close()

    with open(csv_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = 'attachment; filename=' + csv_name + "." + ext
        return response


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

