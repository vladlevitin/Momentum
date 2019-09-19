from django.test import TestCase
from users.forms import StartupRegisterForm
from users.models import User


class StartupRegisterFormTest(TestCase):
    def setUp(self):
        self.form = StartupRegisterForm()
        self.user = User()

    # Redundant, tests package.
    def test_password2_help_text(self):
        self.assertEqual(self.form.fields["password2"].help_text,
                         "Enter the same password as before, for verification.")

    # Too reliant on deep logic -
    # def test_save(self):
