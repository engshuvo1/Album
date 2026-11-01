from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Photos(models.Model):
    category = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProfileImage', default='no_profile.png')
    description = models.TextField(max_length=300,default=True,null=True)
    

    def __str__(self):
        return self.description


class Videos(models.Model):
    title = models.CharField(max_length=250)
    image_thumbnail = models.ImageField(upload_to='image')
    http_link = models.URLField(max_length=200,default=True,null=True)


    def __str__(self):
        return self.title