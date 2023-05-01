from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shopping.models import shopping_index, Shopping_detail, cart

class ShoppingIndexViewTests(TestCase):
    def setUp(self):
        self.url = reverse('shoppingindex')


    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


    def test_filter_by_price(self):
        # Test filtering products by price range
        response = self.client.get(self.url, {'price_min': '0', 'price_max': '10'})
        self.assertEqual(response.status_code, 302)

    def test_filter_by_initial_letter(self):
        # Test filtering products by initial letter
        response = self.client.get(self.url, {'initial_letter': 'A'})
        self.assertEqual(response.status_code, 302)

class AddToCartViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='qwe123456', password='qwe456789')
        self.client.login(username='qwe123456', password='qwe456789')
        self.shopping_item = shopping_index.objects.create(product_name='Hornby 2014 Catalogue', manufacturer='Hornby', price=7.42, country='Denmark')
        self.url = reverse('cart')

    def test_cart(self):
        response = self.client.post(self.url, {'product_name': self.shopping_item.product_name, 'price': self.shopping_item.price})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hornby 2014 Catalogue')
        self.assertContains(response, '7.42')

    def test_remove_from_cart(self):
        # Add item to cart
        response = self.client.post(self.url, {'product_name': self.shopping_item.product_name, 'price': self.shopping_item.price})
        self.assertEqual(response.status_code, 200)

        # Remove item from cart
        remove_url = reverse('remove_from_cart')
        response = self.client.post(remove_url, {'product_name': self.shopping_item.product_name, 'price': self.shopping_item.price})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Hornby 2014 Catalogue')
        self.assertNotContains(response, '7.42')

class RegisterViewTests(TestCase):
    def setUp(self):
        self.url = reverse('register')

    def test_register_new_user(self):
        response = self.client.post(self.url, {
            'username': 'qwe123456',
            'email': '871256465@qq.com',
            'password1': 'qwe456789',
            'password2': 'qwe456789',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_register_existing_user(self):
        # Create a user with the same username as the one we'll try to register
        User.objects.create_user(username='qwe123456', password='qwe456789')

        response = self.client.post(self.url, {
            'username': 'qwe123456',
            'email': '8971256465@qq.com',
            'password1': 'qwe456789',
            'password2': 'qwe456789',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A user with that username already exists.')
