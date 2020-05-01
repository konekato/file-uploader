from django.shortcuts import render
from .models import UploadDetail, UploadFile


def home(request):
    return render(request, 'home.html')

def upload_details(request):
    details = UploadDetail.objects.order_by('-id')
    return render(request, 'upload_details.html',context={
        'details': details,
    })

def upload_file(request, detail_id):
    detail = UploadDetail.objects.get(id=detail_id)
    return render(request, 'upload_file.html', context={
        'detail': detail,
    })