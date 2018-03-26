from .PBlock import PBlock
from collections import deque
import hashlib


class PandaChain:

    def __init__(self):
        self.chain = []
        self.node_transactions = []
        # Creates the first block
        self.create_block(0, 0)

    def create_block(self, proof, prev_hash):
        block = PBlock(len(self.chain), proof,
                       prev_hash, self.node_transactions)
        self.node_transactions = []
        self.chain.append(block)

    def create_transaction(self, sender, receiver, amount):
        self.node_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def get_proof_of_work(self, prev_proof):
        proof = 0
        while self.get_guess(prev_proof, proof) is False:
            proof += 1
        return proof

    def get_guess(self, prev_proof, proof):
        guess = f'{prev_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[2:7] == "10101"

    @property
    def get_last_block(self):
        return self.chain[-1]
