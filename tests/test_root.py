import unittest
from server import root, MESSAGE

class TestRoot(unittest.TestCase):
    def test_message(self):
        self.assertEqual(root(), MESSAGE.encode("utf-8"))

    def test_message_type(self):
        self.assertIsInstance(root(), bytes)

if __name__ == "__main__":
    unittest.main()
