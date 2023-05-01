from django.test import Client, TestCase
from django.urls import reverse
from shopping.models import shopping_index, Shopping_detail, cart


class ShopModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up test data in database
        shopping_index.objects.create(uniq_id='eac7efa5dbd3d667f26eb3d3ab504464', product_name='Hornby 2014 Catalogue', manufacturer='Hornby', price=7.42,
                                      average_review_rating='4.9 out of 5 stars', country='Denmark', img='https://unsplash.com/photos/qBrF1yu5Wys')
        shopping_index.objects.create(uniq_id='e12b92dbb8eaee78b22965d2a9bbbd9f',product_name='HORNBY Coach R4410A BR Hawksworth Corridor 3rd',manufacturer='Hornby', price=39.99,
                                      average_review_rating='5.0 out of 5 stars', country='China',img='https://volcano.si.edu/gallery/photos/GVP-02810.jpg')
        Shopping_detail.objects.create(id=1, date='2022/1/11', uniq_id='eac7efa5dbd3d667f26eb3d3ab504464',
                                       product_name=shopping_index.objects.get(uniq_id='eac7efa5dbd3d667f26eb3d3ab504464'), manufacturer='Hornby',
                                       price=7.42, average_review_rating='4.9 out of 5 stars', city='Aarhus', country='Denmark',
                                       latitude='57.05N', longitude='10.33E')
        Shopping_detail.objects.create(id=2, date='2022/1/12', uniq_id='eac7efa5dbd3d667f26eb3d3ab504464',
                                       product_name=shopping_index.objects.get(uniq_id='eac7efa5dbd3d667f26eb3d3ab504464'), manufacturer='Hornby',
                                       price=6.32, average_review_rating='4.9 out of 5 stars', city='Aarhus', country='Denmark',
                                       latitude='57.05N', longitude='10.33E')


    def test_shopping_index(self):
        shoppingindex = shopping_index.objects.all()
        self.assertEqual(shoppingindex.count(), 2)
        shoppingindex = shopping_index.objects.get(product_name='Hornby 2014 Catalogue')
        self.assertEqual(shoppingindex.manufacturer, "Hornby")

    def test_shopping_detail(self):
        shopping_details = Shopping_detail.objects.all()
        self.assertEqual(shopping_details.count(), 2)
        shopping_detail = Shopping_detail.objects.get(id=1)
        self.assertEqual(shopping_detail.city, "Aarhus")



