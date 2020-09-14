from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    image = models.ImageField(upload_to='')
    discription = models.TextField(max_length=256)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
