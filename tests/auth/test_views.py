"""Flask login client tests."""

from tests.utils import FlaskAppTestCase


class FlaskAuthViewTestCase(FlaskAppTestCase):

    def test_register(self):
        # register a new account
        response = self.client.post(
            "/auth/register",
            data={"email": "john@example.com", "username": "john", "password": "cat"}
        )
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(
            "/auth/login",
            data={"email": "john@example.com", "password": "cat"},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_email(self):
        response = self.client.post(
            "/auth/login",
            data={"email": "com"},
            follow_redirects=True
        )
        self.assertTrue("Invalid email address" in response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_password(self):
        response = self.client.post(
            "/auth/login",
            data={"email": "john@example.com", "password": "1"},
            follow_redirects=True
        )
        self.assertTrue("Invalid email or password." in response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get("/auth/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
