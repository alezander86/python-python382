import unittest
from unittest.mock import patch
import run_service

class TestRunService(unittest.TestCase):
    @patch("os.system")
    def test_run_service(self, mock_system):
        run_service.main()
        mock_system.assert_called_with("python server.py &")

if __name__ == "__main__":
    unittest.main()
