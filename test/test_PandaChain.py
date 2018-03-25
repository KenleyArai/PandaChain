from ..PandaChain import PandaChain
from time import time


class TestPBlock:

    def test_init(self):
        pc = PandaChain()

        # Chain exists and has first block
        assert len(pc.chain) == 1
        # Chain has node transactions
        assert len(pc.node_transactions) == 0

    def test_create_block(self):
        pass

    def test_create_new_transactions(self):
        pass

    def test_create_proof_of_work(self):
        pass

    def test_end_block(self):
        pass
