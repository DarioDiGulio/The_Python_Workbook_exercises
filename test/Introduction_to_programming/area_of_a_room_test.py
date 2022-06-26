from io import StringIO
from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.introduction_to_programming.area_of_a_room import area_of_a_room


class AreaOfARoomTest(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', MagicMock(side_effect=[10.5, 10.5]))
    def test_area_of_a_room(self, fake_system_out: StringIO):
        expected_output = "The area of a room is 110.25 m2\n"

        area_of_a_room()

        self.assertEqual(fake_system_out.getvalue(), expected_output)
