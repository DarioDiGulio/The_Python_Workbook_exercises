from io import StringIO
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.introduction_to_programming.hello import hello


class HelloTest(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', MagicMock(side_effect=['Tom']))
    def test_hello(self, fake_system_out: StringIO):
        expected_output = "Hello, Tom!\n"

        hello()

        self.assertEqual(fake_system_out.getvalue(), expected_output)
