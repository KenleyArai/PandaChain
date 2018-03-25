from .PBlock import PBlock
from collections import deque


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

    def create_transaction(self, sender, reciever, amt):
        self.node_transactions.append({
            'sender': sender,
            'reciever': reciever,
            'amount': amt
        })
