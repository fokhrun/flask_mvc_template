
from tests.utils import FlaskAppTestCase
from app.auth.forms import RegistrationForm
import wtforms


class TestRegistrationForm(FlaskAppTestCase):

    def test_registration_wrong_email_format(self):
        form = RegistrationForm(email="123")
        self.assertFalse(form.validate())

    def test_registration_validate_email(self):
        email = "ab@123.c"
        username = "ab"
        password = "123"
        self.client.post(
            "/auth/register",
            data={"email": email, "username": username, "password": password, "password2": password}
        )

        form = RegistrationForm(email=email, username=username, password=password, password2=password)
        self.assertRaises(wtforms.validators.ValidationError, form.validate_email, form.email)

    def test_registration_validate_username(self):
        email = "ab@123.c"
        username = "ab"
        password = "123"
        self.client.post(
            "/auth/register",
            data={"email": email, "username": username, "password": password, "password2": password}
        )

        form = RegistrationForm(email="xx@x.x", username=username, password=password, password2=password)
        self.assertRaises(wtforms.validators.ValidationError, form.validate_username, form.username)
