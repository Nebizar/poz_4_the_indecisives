from django.db import models

# Create your models here.
class Item(models.Model):
    picture = models.TextField()
    name = models.TextField()
    price = models.CharField(max_length = 7)
    cebulions = models.IntegerField()
    category_id = models.CharField(max_length = 10)
