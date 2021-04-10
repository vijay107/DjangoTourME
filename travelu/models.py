from django.db import models

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    link = models.URLField(max_length=200)
    offer = models.BooleanField(default=False)
