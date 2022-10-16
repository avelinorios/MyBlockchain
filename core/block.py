from core.b_transaction import Transaction


class Block:
    """
    Contains a group of transactions.
    :param transactions: a list of Transaction.
    :param hash: the Block hash code.
    :param previous_block: the hash of the block that precedes this one.
    """
    def __init__(self, transactions, previous_block):
        self.transactions = transactions
        self.hash = self.calculate_hash()
        self.previous_block = previous_block

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def calculate_hash(self):
        return 1234

