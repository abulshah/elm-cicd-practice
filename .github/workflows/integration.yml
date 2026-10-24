
import unittest
from urllib.request import urlopen


class HttpIntegrationTests(unittest.TestCase):

    def test_health_endpoint(self):

        with urlopen(
            "http://127.0.0.1:8000/health",
            timeout=5
        ) as response:

            self.assertEqual(response.status, 200)

            self.assertEqual(
                response.read().decode(),
                "healthy"
            )
