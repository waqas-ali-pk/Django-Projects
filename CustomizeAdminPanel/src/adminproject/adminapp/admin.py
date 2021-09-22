from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet

class AdminSnippet(admin.ModelAdmin):
    change_list_template = 'admin/snippets/snippet_change_list.html'

admin.site.register(Snippet, AdminSnippet)
admin.site.unregister(Group)

