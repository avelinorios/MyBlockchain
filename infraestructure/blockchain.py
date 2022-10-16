from core.block import Block


class Blockchain:
    def __init__(self):
        self.blocks = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        """
        Creates the first block of the blockchain
        :return: The initial Block
        """
        return Block([], None)

    @property
    def last_block(self):
        return self.blocks[-1]
