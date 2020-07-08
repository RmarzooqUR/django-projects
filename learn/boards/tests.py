from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, boardsHome

# Create your tests here.
class boardsTests(TestCase):
    def test_board_status(self):
        url = reverse('boardsHome')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_views(self):
        view = resolve('/')
        view2 = resolve('/boards/')
        self.assertEquals(view.func,home)
        self.assertEquals(view2.func,boardsHome)