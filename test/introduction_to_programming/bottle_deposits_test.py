from io import StringIO
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.introduction_to_programming.bottle_deposits import bottle_deposits_refund


class BottleDepositsTest(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', MagicMock(side_effect=[10, 15]))
    def test_bottle_deposits_refund(self, fake_system_out: StringIO):
        expected_output = "The refund is $4.75\n"

        bottle_deposits_refund()

        self.assertEqual(fake_system_out.getvalue(), expected_output)
