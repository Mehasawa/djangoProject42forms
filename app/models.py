from django.db import models

# Create your models here.

class modelComent(models.Model):
    name = models.CharField(max_length=100,)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    email = models.EmailField(blank=True, null=True)

class modelEda(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class modelChoise(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    eda = models.ForeignKey(modelEda, on_delete=models.CASCADE)
    dopTomato = models.BooleanField(default=False)
    dopCheese = models.BooleanField(default=False)
    dopKolbasa = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

