from ..PandaChain import PBlock


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
