from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from shopping.forms import RegistrationForm

class RegistrationFormTests(TestCase):
    def test_registration_form(self):
        form_data = {
            'username': 'qwe123456',
            'email': '871256465@qq.com',
            'password1': 'def456789',
            'password2': 'def456789'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save(commit=False)
        user.save()
        self.assertEqual(user.username, 'qwe123456')
        self.assertEqual(user.email, '871256465@qq.com')
        self.assertTrue(user.check_password('def456789'))
