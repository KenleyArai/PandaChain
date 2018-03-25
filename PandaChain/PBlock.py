import time
import hashlib


class PBlock:

    def __init__(self, index, proof, prev_hash=None, transactions=None):
        self.index = index
        self.proof = proof
        self.prev_hash = prev_hash
        self.transactions = transactions or []
        self.timestamp = time.time()

    def get_string(self):
        return "{}{}{}{}{}".format(self.index, self.proof, self.prev_hash, self.transactions, self.timestamp)

    @property
    def get_block_hash(self):
        return hashlib.sha256(self.get_string().encode()).hexdigest()
