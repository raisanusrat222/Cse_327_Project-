from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from metro_app.models import Employee 
from metro_app.forms import RegForm
# from test_forms import TestForms



class SetupTest(TestCase):
    def setUp(self):
        self.register_url = reverse('empregister')
        self.user = {
            'first_name': 'zoro',
            'last_name': 'koro',
            'phone': '01954565327',
            'nid': '1342356748',
            'address': 'olympas'
        }

        return super().setUp()

class RegisterTest(SetupTest):

    def test_can_user_register(self):
        response = self.client.post(self.register_url, self.user, format = 'text/html')
        self.assertEqual(response.status_code,200) 

    def test_POST_adds_user_data(self):
        response = self.client.post(self.register_url, self.user, format = 'text/html')
        self.object1 = Employee.objects.create(
           First_Name = self.user
        )
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.object1.First_Name, self.user )    

    def test_POST_adds_authentication_data(self):
        form = RegForm(data={
            'username': 'garelt',
            'email': 'riv@gmail.com',
            'password1': 'bloody123',
            'password2': 'bloody123'
        })

        self.assertTrue(form.is_valid())

        # response = self.client.post(self.register_url, form)
        self.object2 = User.objects.create(
           username = form
        )
        # self.assertEqual(response.status_code,302)
        self.assertEqual(self.object2.username, form )        