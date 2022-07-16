from email.policy import default
from django.db import models

# Create your models here.


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    intro = models.TextField(max_length=1000,default="This is the intro")
    desc = models.TextField(max_length=4000)
    author =models.CharField(max_length=50)
    slug =models.CharField(max_length=50,default="")
    release_date = models.DateField()
    tumbnail = models.ImageField(upload_to='images/',default="logo.png")
    img1 = models.ImageField(upload_to='images/',default="logo.png")
    img2 = models.ImageField(upload_to='images/',default="logo.png")
    img3 = models.ImageField(upload_to='images/',default="logo.png")


    def __str__(self) :
        return self.name


class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=4000)
    author =models.CharField(max_length=50)
    slug =models.CharField(max_length=50,default="")
    release_date = models.DateField()
    tumbnail = models.ImageField(upload_to='images/',default="logo.png")
    
    def __str__(self) :
        return self.title

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=4000)
    email =models.CharField(max_length=50)
   
    
    def __str__(self) :
        return self.name