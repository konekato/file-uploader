from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    form = UploadFileForm()

    # POSTED
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        print(form.is_bound)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.detail_id = detail_id
            obj.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print('error')

    return render(request, 'upload_file.html', context={
        'detail': detail,
        'form': form,
    })