from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True)
    date = models.DateField(null=True)
    def __str__(self): 
        return self.headline
