from django.shortcuts import render
from .models import UploadDetail, UploadFile
from .forms import UploadFileForm

def home(request):
    return render(request, 'home.html')

def upload_details(request):
    details = UploadDetail.objects.order_by('-id')
    return render(request, 'upload_details.html',context={
        'details': details,
    })

def upload_file(request, detail_id):
    detail = UploadDetail.objects.get(id=detail_id)
    form = UploadFileForm
    return render(request, 'upload_file.html', context={
        'detail': detail,
        'form': form,
    })