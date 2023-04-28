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
    img = models.TextField(default='default_value_here')

    def __str__(self):
            return f'{self.uniq_id}, {self.product_name}, {self.manufacturer}, {self.price}, {self.average_review_rating}, {self.country}, {self.img}'

class Shopping_detail(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.TextField()
    uniq_id = models.TextField()
    product_name = models.ForeignKey('shopping_index',on_delete=models.CASCADE)
    manufacturer = models.TextField()
    price = models.FloatField()
    average_review_rating = models.TextField()
    city = models.TextField()
    country = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    def __str__(self):
            return f'{self.id}, {self.date}, {self.uniq_id}, {self.product_name},{self.manufacturer},{self.price},{self.average_review_rating},{self.city},{self.country},{self.latitude},{self.longitude}'
class cart(models.Model):
    product_id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    product_name = models.TextField()
    sale_place = models.TextField()
    add_to_chart = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_id}, {self.price}, {self.product_name}, {self.sale_place}, {self.add_to_chart}'


