import unittest
from infraestructure.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):

    def test_genesis_block_creation(self):
        blockchain_to_test = Blockchain()
        self.assertEqual(len(blockchain_to_test.blocks), 1, "Should be 1")


if __name__ == '__main__':
    unittest.main()
