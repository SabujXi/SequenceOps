from unittest import TestCase
from sequenceops import Sequence


class TestSequence(TestCase):
    def test_equals(self):
        assert Sequence.equals([1, 2], (1, 2))
        assert Sequence.equals([1, 2], [1, 2])
        assert Sequence.equals([1, 2], list((1, 2)))

    def test_startswith(self):
        assert Sequence.startswith((1, 2), [1, ])

    def test_endswith(self):
        assert Sequence.endswith((1, 2), (2, ))

    def test_lstrip(self):
        assert Sequence.lstrip([1, 2, 3], [1, 2, 3]) == []
        assert Sequence.lstrip([1, 2, 3], [2, 2, 3]) == [1, 2, 3]

    def test_rstrip(self):
        assert Sequence.rstrip([1, 2, 3], [2, 3]) == [1], f'{Sequence.rstrip([1, 2, 3], [2, 3])}'
        assert Sequence.rstrip([1, 2, 3], [2, 2, 3]) == [1, 2, 3]

    def test_strip(self):
        self.fail()
