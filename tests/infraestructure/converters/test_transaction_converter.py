import unittest

from core.b_transaction import Transaction
from infraestructure.converters.transaction_converter import TransactionConverter


class TestTransactionConverter(unittest.TestCase):

    def setUp(self) -> None:
        self.transaction_expected = Transaction('sender1', 'receiver1', 900)

    def test_json_to_transaction(self):
        json = {'sender': 'sender1', 'receiver': 'receiver1', 'amount': 900}
        transaction = TransactionConverter().from_json(json)
        self.assertEqual(transaction.sender, self.transaction_expected.sender)
        self.assertEqual(transaction.receiver, self.transaction_expected.receiver)
        self.assertEqual(transaction.amount, self.transaction_expected.amount)

    def test_transaction_without_sender(self):
        json = {'sender': '', 'receiver': 'receiver1', 'amount': 900}
        self.assertRaises(Exception, TransactionConverter().from_json, json)

    def test_transaction_without_receiver(self):
        json = {'sender': 'sender1', 'receiver': '', 'amount': 900}
        self.assertRaises(Exception, TransactionConverter().from_json, json)

    def test_transaction_without_amount_zero(self):
        json = {'sender': '', 'receiver': 'receiver1', 'amount': 0}
        self.assertRaises(Exception, TransactionConverter().from_json, json)

    def test_transaction_without_amount_less_than_zero(self):
        json = {'sender': '', 'receiver': 'receiver1', 'amount': -20}
        self.assertRaises(Exception, TransactionConverter().from_json, json)
