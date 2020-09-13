from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    image = models.ImageField(upload_to='')
    discription = models.TextField(max_length=256)
    pub_date = models.DateTimeField(auto_now_add=True)
