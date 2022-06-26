from io import StringIO
from unittest import mock, TestCase

from src.introduction_to_programming.hello import hello


class HelloTest(TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_hello(self, fake_system_out: StringIO):
        expected_output = "Hello, Tom!\n"

        with mock.patch('builtins.input', return_value='Tom'):
            hello()

            self.assertEqual(fake_system_out.getvalue(), expected_output)
