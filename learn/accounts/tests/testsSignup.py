from django.test import TestCase
from django.urls import resolve, reverse
from ..forms import signUpForm
from django.contrib.auth.models import User
from ..views import signup
# Create your tests here.

class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def testSignupReverse(self):
        self.assertEqual(self.response.status_code, 200)

    def testSignupResolve(self):
        view = resolve('/accounts/')
        self.assertEqual(view.func, signup)

    def testCsrfTruth(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def testFormInstance(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, signUpForm)


class SignupLogic(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username' : 'testuser',
            'email': 'example@example.com',
            'password1' : 'eQw8pK8dsLhFMBT',
            'password2' : 'eQw8pK8dsLhFMBT'
        }
        self.response = self.client.post(url, data)
        self.redirected = reverse('boardsHome')

    def test_signup(self):
        self.assertRedirects(self.response, self.redirected)
    
    def testUserCreation(self):
        self.assertTrue(User.objects.exists())
    
    def testAuthenticated(self):
        response = self.client.get(self.redirected)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class unsuccessfulSignup(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {}
        self.response = self.client.post(url, data)
    
    def testFormErrors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
    
    def testNonCreationUser(self):
        self.assertFalse(User.objects.exists())