from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class UploadDetail(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class UploadFile(models.Model):
    file = models.FileField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    detail = models.ForeignKey(UploadDetail, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.url
