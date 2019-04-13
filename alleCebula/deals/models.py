from django.db import models

# Create your models here.
class Item(models.Model):
    picture = models.TextField()
    name = models.TextField()
    price = models.CharField(max_length = 7)
    cebulions = models.IntegerField()
    category_id = models.CharField(max_length = 10)
    
class Comment(models.Model):
    product_id = models.ForeignKey(Item, on_delete = models.CASCADE)
    content = models.TextField()
    nick = models.TextField()
