from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('base',base,name='base'),
    path('main',main,name='main'),
    path('image',image,name='image'),
    path('videos',Video,name='videos'),
    path('image-search',image_search,name='image-search'),    
   
]