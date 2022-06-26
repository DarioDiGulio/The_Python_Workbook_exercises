from io import StringIO
from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.introduction_to_programming.tax_and_tip import TAX, TIP, ticket


class TaxAndTipTest(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', MagicMock(side_effect=[750]))
    def test_ticket(self, fake_system_out: StringIO):
        expected_output = "Tax and Trip\n" \
                          "The total cost of your meal is $750.00\n" \
                          f"The tax is {self.tax_amount:.2f}\n" \
                          f"The tip is {self.tip_amount:.2f}\n" \
                          f"The total cost of your meal with tax is ${self.total_cost:.2f}\n"

        ticket()

        self.assertEqual(fake_system_out.getvalue(), expected_output)

    tax_amount = 750 * TAX
    tip_amount = (750 + tax_amount) * TIP
    total_cost = 750 + tax_amount + tip_amount
