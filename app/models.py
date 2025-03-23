from django.db import models

# Create your models here.

class modelComent(models.Model):
    name = models.CharField(max_length=100,)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    email = models.EmailField(blank=True, null=True)