from django.test import SimpleTestCase
from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import *
from .models import *
import json


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_Complains_url_is_resolved(self):
        url = reverse('Complains')
        self.assertEquals(resolve(url).func, complains)


    def test_AfterComplains_url_is_resolved(self):
        url = reverse('AfterComplain')
        self.assertEquals(resolve(url).func, aftercomplain)

    def test_SeeComplains_url_is_resolved(self):
        url = reverse('SeeComplains')
        self.assertEquals(resolve(url).func, seecomplains)

class TestViews(TestCase):

    def setup(self):
        self.client = Client()
        self.aftercomplain_url = reverse('AfterComplain')

    def test_complains(self):
        client = Client()

        response = client.get(reverse('Complains'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Ticket/Complain.html')

    def test_aftercomplains_Post(self):
        self.client = Client()
        self.aftercomplain_url = reverse('AfterComplain')

        response= self.client.post(self.aftercomplain_url, {
            'fname':'Anisha',
            'contact':'get@gmail.com',
            'subject':'Your Website is useless'
        })

    def test_seecomplains(self):
        client = Client()

        response = client.get(reverse('SeeComplains'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Ticket/SeeComplain.html')



