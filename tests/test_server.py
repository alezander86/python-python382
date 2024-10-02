import unittest
from server import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        response = self.app.get("/api/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, DEMO!\n")

if __name__ == "__main__":
    unittest.main()
