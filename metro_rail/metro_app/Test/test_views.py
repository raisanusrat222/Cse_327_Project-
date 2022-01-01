from django.test import TestCase,Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from metro_app.models import schedule_check
import json

class TestViews(TestCase):
    def setUp(self):
        User(username="random",password="random1234").save()
        user = User.objects.get(username="random")
        self.client = Client()
    def test_login_POST(self):
        response = self.client.post("login",{
            "username":"",
            "password":""
        })
        return response
    def test_schedule_checks_GET(self):
        client=Client()
        response=client.get(reverse('scheck'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'metro_app/schedule_check.html')

