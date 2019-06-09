from .models import FileUpload
from django import forms


class FileUploadCreateForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        exclude = ('id', 'file_name',
                   'created_on', 'created_user_id',
                   'modified_on', 'modified_user_id')
        labels = {
            'file': 'Select a file'
        }

