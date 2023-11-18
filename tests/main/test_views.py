
from tests.utils import FlaskAppTestCase


class FlaskIndexViewTestCase(FlaskAppTestCase):

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Stranger" in response.data)
