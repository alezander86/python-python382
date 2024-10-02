import unittest
from setup import VersionCommand
from version import __version__
from io import StringIO
import sys

class TestSetup(unittest.TestCase):
    def test_version_command(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            cmd = VersionCommand()
            cmd.run()
            output = out.getvalue().strip()
            self.assertEqual(output, __version__)
        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()
