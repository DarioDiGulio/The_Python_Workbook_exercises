import unittest
from io import StringIO
from unittest import mock

from src.introduction_to_programming.mailing_address import mailing_address


class MailingAddressTest(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_mailing_address(self, fake_system_out):
        expected_output = 'Dario Di Gulio\n123 Main St.\nAnytown, NY 12345\n'

        mailing_address()

        self.assertEqual(fake_system_out.getvalue(), expected_output)
