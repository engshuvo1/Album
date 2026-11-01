from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q


# Create your views here.
def home (request):
    return render (request,'photos/home.html')


def base(request):

    forms = PhotosForms()
    if request.method =='POST':
        forms = PhotosForms(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,'successfully-Save')
            return redirect('image')


    Context = {
        'form': forms

    }

    return render(request,'photos/base.html',Context)


def main(request):
    forms = VideosForms()
    if request.method =='POST':
        forms = VideosForms(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,'successfully-Save')
            return redirect('videos')


    Context = {
        'forms': forms

    }

    return render(request,'photos/main.html',Context)


def image(request):
    photos = Photos.objects.all()

    context = {
        'photos' : photos
    }
    return render (request,'photos/image.html',context)


def Video(request):
    image = Videos.objects.all()

    context = {
        'image' : image
    }
    return render (request,'photos/videos.html',context)


def image_search(request):
    category = request.GET['images-search']
    photos = Photos.objects.filter(description__icontains=category)
    
    context ={
          'photos': photos
    }
    return render (request,'photos/image-search.html',context)