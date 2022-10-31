import json

from core.b_transaction import Transaction
from hashlib import sha256

class Block:
    """
    Contains a group of transactions.
    :param transactions: a list of Transaction.
    :param previous_block: the hash of the block that precedes this one.
    :parameter nonce: number to complete mining process
    """

    def __init__(self, transactions, previous_block):
        self.transactions = transactions
        self.previous_block = previous_block
        self.nonce = None

    def __repr__(self):
        return f"nonce: {self.nonce}, previous_block: {self.previous_block}, hash: {self.hash}, transactions: {self.transactions}"

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def calculate_hash(self):
        block_string = json.dumps(self.toJson)
        return sha256(block_string.encode()).hexdigest()


    @property
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)