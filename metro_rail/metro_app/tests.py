from django.test import TestCase
from django.contrib.auth.models import user

# Create your tests here.
class BaseTest(TestCase):
    self.login_url=reverse('login')
class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code=200)
        self.assertTemplateUsed(response,'auth./login.html')
    def test_login_success(self):
        self.client.post(self.register_url,self.user,format="text/html")
        user=User.objects.filter(user_name=self.user[user_name]).first()
        user.is_active=True
        user.save()
        response=self.client