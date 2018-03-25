from ..PandaChain import PBlock
import time
import hashlib


class TestPBlock:

    def test_init(self):
        test_block = PBlock(27, 11)

        # Check index exists
        assert test_block.index == 27
        # Check proof exists
        assert test_block.proof == 11
        # Check previous hash exists
        assert test_block.prev_hash == None
        # Check transactions exist
        assert len(test_block.transactions) == 0

    def test_get_string(self):
        test_block = PBlock(27, 11)

        # Freezing time so we can test the block
        t = time.time()
        test_block.timestamp = t

        # Creating the string that should be the output get_string
        test_string = "{}{}{}{}{}".format(27, 11, None, [], t)
        assert test_string == test_block.get_string()

    def test_get_hash(self):
        test_block = PBlock(27, 11)

        # Freezing time so we can test the block
        t = time.time()
        test_block.timestamp = t

        # Creating the string that should be the output get_string
        test_string = "{}{}{}{}{}".format(27, 11, None, [], t)
        test_block_hash = hashlib.sha256(test_string.encode()).hexdigest()

        assert test_block_hash == test_block.get_block_hash
