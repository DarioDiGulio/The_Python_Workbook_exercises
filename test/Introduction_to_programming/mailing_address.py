import unittest

from src.introduction_to_programming.mailing_address import mailing_address
from test.Testing.StandardOutput import out_put


class MailingAddressTest(unittest.TestCase):

    def test_mailing_address(self):
        self.assertEqual(out_put(mailing_address), 'Dario Di Gulio\n123 Main St.\nAnytown, NY 12345')

