from io import StringIO
from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.introduction_to_programming.widgets_and_gizmos import widgets_and_gizmos


class WidgetsAndGizmosTest(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', MagicMock(side_effect=[3, 5]))
    def test_something(self, fake_system_out: StringIO):
        expected_output = 'The total weight of the order is 785 grams.\n'

        widgets_and_gizmos()

        self.assertEqual(fake_system_out.getvalue(), expected_output)
