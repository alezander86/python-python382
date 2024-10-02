import unittest
from version import __version__

class TestVersion(unittest.TestCase):
    def test_version_format(self):
        self.assertRegex(__version__, r"^\d+\.\d+\.\d+(-RC\.\d+)?$")

if __name__ == "__main__":
    unittest.main()
