from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UploadDetail, UploadFile
from .forms import UploadFileForm


def home(request):
    details = UploadDetail.objects.order_by('-id')
    return render(request, 'home.html', context={
        'details': details,
    })

def user_profile(request):
    return render(request, 'user_profile.html')

# app
def upload_details(request):
    details = UploadDetail.objects.order_by('-id')
    return render(request, 'upload_details.html', context={
        'details': details,
    })


def upload_file(request, detail_id):
    user_id = request.user.id

    details = UploadDetail.objects.order_by('-id')
    detail = UploadDetail.objects.get(id=detail_id)
    form = UploadFileForm()
    uploaded_files = UploadFile.objects.filter(
        detail_id=detail_id, user_id=user_id).order_by('-id')

    # POSTED
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.detail_id = detail_id
            obj.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print('error')

    return render(request, 'upload_file.html', context={
        'details': details,
        'detail': detail,
        'form': form,
        'uploaded_files': uploaded_files,
    })


def upload_history(request):
    user_id = request.user.id

    details = UploadDetail.objects.order_by('-id')
    uploaded_files = UploadFile.objects.filter(user_id=user_id).order_by('-id')

    return render(request, 'upload_history.html', context={
        'details': details,
        'uploaded_files': uploaded_files,
    })
