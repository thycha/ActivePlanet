from django.db import models
from U_Auth.models import User

# Create your models here.

BANNER_TYPES = [('Mobile','Mobile'),('System','System')]

class Banner(models.Model):
    Date = models.DateField(auto_now_add=True)
    Banner_Type = models.CharField(max_length=10,choices=BANNER_TYPES)
    Image = models.ImageField(null=True,upload_to='Banners')

class Gallery_Image(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Gallery')

class Partners(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Partners')

class Schools(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Partners')

class Event(models.Model):
    Added_Date = models.DateField(auto_now_add=True)

    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Description = models.TextField()
    Image = models.ImageField(null=True,upload_to='Events')

    def __str__(self):
        return self.Name
    
class Review(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100,null=True)
    Rating = models.IntegerField(default=0)
    Description = models.TextField()

class Enquiry(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=20,null=True)
    Description = models.TextField()