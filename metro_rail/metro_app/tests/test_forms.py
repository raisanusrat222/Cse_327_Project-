from django.test import TestCase
from metro_app.forms import RegForm

class TestForms(TestCase):
    def test_RegForm_valid_data(self):
        form = RegForm(data={
            'username': 'fahim',
            'email': 'fahim@gmail.com',
            'password1': 'bloody123',
            'password2': 'bloody123'
        })

        self.assertTrue(form.is_valid())

    def test_RegForm_invalid_data1(self):
        form = RegForm(data={
            'username': 'fahim',
            'email': 'fahim@gmail.com',
            'password1': 'bloody123',
            'password2': 'bloody'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals (len (form.errors), 1)

    def test_RegForm_invalid_data2(self):
        form = RegForm(data={
            'username': 'fahim',
            'email': 'fahim',
            'password1': 'bloody123',
            'password2': 'bloody123'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals (len (form.errors), 1)

    def test_RegForm_no_data(self):
        form = RegForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals (len (form.errors), 3)