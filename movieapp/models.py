from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movieapp(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='movieapp/images/', blank=True)
    url = models.URLField(blank=True)
    
class Review(models.Model):
    text = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    movieapp = models.ForeignKey( Movieapp,on_delete=models.CASCADE, blank=True)
    watchAgain = models.BooleanField() 
    
    def __str__(self): 
        return self.text