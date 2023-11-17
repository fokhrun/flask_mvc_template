"""Flask login client tests."""

import unittest
from app import create_app, db
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

    def test_logout(self):
        response = self.client.get("/auth/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
