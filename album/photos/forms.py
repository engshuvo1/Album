from django import forms
from .models import *



class PhotosForms(forms.ModelForm):
   

    class Meta:    
        
        model = Photos
        
        fields = '__all__'



class VideosForms(forms.ModelForm):
   

    class Meta:    
        
        model = Videos
        
        fields = '__all__'