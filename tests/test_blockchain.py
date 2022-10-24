import unittest

from core.block import Block
from infraestructure.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):

    def test_genesis_block_creation(self):
        blockchain_to_test = Blockchain()
        self.assertEqual(len(blockchain_to_test.blocks), 1, "Should be 1")

    def test_last_block(self):
        blockchain_to_test = Blockchain()
        genesis_block = blockchain_to_test.blocks[0]
        self.assertEqual(blockchain_to_test.last_block.hash, genesis_block.hash)

        block_1 = Block([], genesis_block.hash)
        block_1.calculate_hash()
        blockchain_to_test.blocks.append(block_1)
        self.assertEqual(blockchain_to_test.last_block.hash, block_1.hash)


if __name__ == '__main__':
    unittest.main()
