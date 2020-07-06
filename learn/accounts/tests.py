from django.test import TestCase
from django.urls import resolve,reverse
from .views import signup
# Create your tests here.
class signUpTest(TestCase):
    def signupReverse(self):
        url = reverse('')
        response = self.client.get(url)
        self.assertEquals(response.status_code, '200')

    def signupResolve(self):
        view = resolve('')
        self.assertEquals(view.func, signup)