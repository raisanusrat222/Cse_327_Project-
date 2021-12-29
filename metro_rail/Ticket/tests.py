from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import *


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

