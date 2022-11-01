import unittest

from core.b_transaction import Transaction
from core.block import Block
from infraestructure.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):

    def setUp(self) -> None:
        self.blockchain_to_test = Blockchain()

        transaction1 = Transaction('sender1', 'receiver1', 20.5)
        transaction2 = Transaction('sender2', 'receiver2', 5.2)
        transaction3 = Transaction('sender3', 'receiver3', 880.0)
        transaction4 = Transaction('sender4', 'receiver4', 120.0)

        self.blockchain_to_test.transaction_pool.append(transaction1)
        self.blockchain_to_test.transaction_pool.append(transaction2)
        self.blockchain_to_test.transaction_pool.append(transaction3)
        self.blockchain_to_test.transaction_pool.append(transaction4)

    def test_genesis_block_creation(self):
        self.assertEqual(len(self.blockchain_to_test.blocks), 1, "Should be 1")

    def test_last_block(self):
        genesis_block = self.blockchain_to_test.blocks[0]
        self.assertEqual(self.blockchain_to_test.last_block.hash, genesis_block.hash)

        block_1 = Block([], genesis_block.hash)
        block_1.hash = block_1.calculate_hash()
        self.blockchain_to_test.blocks.append(block_1)
        self.assertEqual(self.blockchain_to_test.last_block.hash, block_1.hash)

    def test_mine(self):
        self.blockchain_to_test.mine()
        self.assertEqual(len(self.blockchain_to_test.transaction_pool), 1)
        self.assertEqual(len(self.blockchain_to_test.blocks), 2)
        self.assertEqual(self.blockchain_to_test.difficulty, 2)

    def test_mine_with_1_transaction(self):
        del self.blockchain_to_test.transaction_pool[:3]
        self.blockchain_to_test.mine()
        self.assertEqual(len(self.blockchain_to_test.transaction_pool), 0)
        self.assertEqual(len(self.blockchain_to_test.blocks), 2)
        self.assertEqual(self.blockchain_to_test.difficulty, 2)

    def test_mine_without_transactions(self):
        del self.blockchain_to_test.transaction_pool[:4]
        self.assertRaises(Exception, self.blockchain_to_test.mine()
                          )


if __name__ == '__main__':
    unittest.main()
