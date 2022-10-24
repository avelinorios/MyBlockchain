from core.b_transaction import Transaction
from core.block import Block


class Blockchain:

    def __init__(self):
        self.blocks = [self.create_genesis_block()]
        self.transaction_pool = []

    @staticmethod
    def create_genesis_block():
        """
        Creates the first block of the blockchain
        :return: The initial Block
        """
        genesis_block = Block([], None)
        genesis_block.calculate_hash()
        return genesis_block

    def add_transaction(self, transaction: Transaction):
        self.transaction_pool.append(transaction)

    def mine(self):
        """
        Ejecuta la prueba de trabajo
        :return:
        """
        self.create_new_block()

    def _create_new_block(self):
        transactions = self.transaction_pool[:3]
        del self.transaction_pool[3:]

        block = Block(transactions, self.last_block)

    @property
    def last_block(self):
        return self.blocks[-1]
