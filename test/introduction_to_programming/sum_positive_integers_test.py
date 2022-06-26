from io import StringIO
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.introduction_to_programming.sum_positive_integers import sum_integers_to_n


class SumPositiveIntegersTest(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', MagicMock(side_effect=[3]))
    def test_sum_integers_by_input(self, fake_system_out: StringIO):
        expected_output = "6\n"

        sum_integers_to_n()

        self.assertEqual(fake_system_out.getvalue(), expected_output)
