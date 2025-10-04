import unittest
from seq import Seq


class TestSeq(unittest.TestCase):

    def test_dna_sequence(self):
        seq = Seq("test_dna", "ATCGATCG")
        self.assertEqual(seq.alphabet_validation(), "ДНК")
        self.assertEqual(len(seq), 8)

    def test_protein_sequence(self):
        seq = Seq("test_protein", "MALWMRLL")
        self.assertEqual(seq.alphabet_validation(), "белковый")

    def test_empty_sequence(self):
        seq = Seq("empty", "")
        self.assertEqual(seq.alphabet_validation(), "пустая")


if __name__ == '__main__':
    unittest.main()