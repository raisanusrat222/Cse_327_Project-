from django.test import SimpleTestCase
from django.urls import reverse, resolve
from metro_app.views import pregister, empregister, premiumpage, TicketValid

class TestUrls(SimpleTestCase):

    def test_pregister_url_resolves(self):
        url = reverse('pregister')      
        self.assertEquals(resolve(url).func, pregister)