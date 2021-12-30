from django.test import SimpleTestCase
from django.urls import reverse,resolve
from metro_app.views import loginPage,logoutUser

class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,loginPage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logoutUser)
        
        
       
