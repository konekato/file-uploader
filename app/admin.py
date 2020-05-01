from django.contrib import admin
from .models import UploadDetail, UploadFile

admin.site.register(UploadDetail)
admin.site.register(UploadFile)