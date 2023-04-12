from django.db import models
from django.conf import settings
# Create your models here.

class shopping_index(models.Model):
    uniq_id = models.TextField()
    product_name = models.TextField(primary_key=True)
    manufacturer = models.TextField()
    price = models.FloatField()
    average_review_rating = models.TextField()
    country = models.TextField()

    def __str__(self):
            return f'{self.uniq_id}, {self.product_name}, {self.manufacturer}, {self.price}, {self.average_review_rating}, {self.country}'