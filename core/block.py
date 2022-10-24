import json

from core.b_transaction import Transaction
from hashlib import sha256

class Block:
    """
    Contains a group of transactions.
    :param transactions: a list of Transaction.
    :param hash: the Block hash code.
    :param previous_block: the hash of the block that precedes this one.
    """

    def __init__(self, transactions, previous_block):
        self.hash = None
        self.transactions = transactions
        self.previous_block = previous_block

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        self.hash = sha256(block_string.encode()).hexdigest()
