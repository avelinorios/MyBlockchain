from core.b_transaction import Transaction
from core.block import Block


class Blockchain:

    def __init__(self):
        self.blocks = [self.create_genesis_block()]
        self.transaction_pool = []
        self.difficulty = 1

    @staticmethod
    def create_genesis_block():
        """
        Creates the first block of the blockchain
        :return: The initial Block
        """
        genesis_block = Block([], None)
        genesis_block.hash = genesis_block.calculate_hash()
        return genesis_block

    def add_transaction(self, transaction: Transaction):
        self.transaction_pool.append(transaction)

    def mine(self):
        """
        Starts mining using proof of work
        :return:
        """
        print("starts mining...")
        block = self._create_new_block()
        proof_hash = self._proof_of_work(block)
        self._add_block_to_blockchain(block, proof_hash)
        self.difficulty += 1

    def _add_block_to_blockchain(self, block, proof_hash):
        """
        Add new mined block to the blockchain if proof is valid
        :param block: The block to add.
        :return: True if block is added. False otherwise.
        """
        if not self._is_valid_proof(proof_hash, block):
            return False
        block.hash = proof_hash
        self.blocks.append(block)
        return True

    def _is_valid_proof(self, proof_hash, block):
        if proof_hash.startswith('0' * self.difficulty) \
                and proof_hash == block.calculate_hash():
            return True
        return False

    def _proof_of_work(self, block: Block):
        """
        Try to find a hash with a nonce that solves the blockchain difficulty.
        """
        block.nonce = 0

        generated_hash = block.calculate_hash()
        while not generated_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            generated_hash = block.calculate_hash()
            print(f"nonce: {block.nonce}, hash: {generated_hash}")

        return generated_hash

    def _create_new_block(self) -> Block:
        transactions = self.transaction_pool[:3]
        if transactions is []:
            raise Exception("There is no transaction in the blockchain.")
        del self.transaction_pool[:3]
        return Block(transactions, self.last_block.hash)

    @property
    def last_block(self):
        return self.blocks[-1]
