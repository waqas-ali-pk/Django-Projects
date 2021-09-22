from django.db import models


class Snippet(models.Model):
    name = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        