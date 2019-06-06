from django.core.validators import FileExtensionValidator
from django.db import models
import datetime, os
# Create your models here.


def photo_path(instance, filename):

    base_file_name, file_extension = os.path.splitext(filename)
    random = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %f")
    return 'images/{basename}_{random}{ext}'.format(
        basename=base_file_name, random=random, ext=file_extension)


class FileUpload(models.Model):

    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=150, blank=True)
    file = models.FileField(upload_to=photo_path, validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'png', 'bmp'])], blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=True)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return u'/file/%d' % self.id

