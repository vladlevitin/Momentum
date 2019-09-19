from django.test import TestCase
from users.views import startupsview
from users.forms import StartupRegisterForm
from django.urls import reverse

class StartupsviewTest(TestCase):

    # Probably redundant, testing of well-tested package.
    def test_register_startup(self):
        self.form = StartupRegisterForm()
        url = reverse("register_startup")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
