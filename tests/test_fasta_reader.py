import unittest
import os
import tempfile
from fasta_reader import FastaReader
from seq import Seq


class TestFastaReader(unittest.TestCase):

    def setUp(self):
        # Создаем временный FASTA файл для тестов
        self.fasta_content = """>sequence1
ATCGATCGATCG
>sequence2
GCTAGCTAGCTA"""

        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.fasta', delete=False)
        self.temp_file.write(self.fasta_content)
        self.temp_file.close()

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_is_fasta_valid(self):
        reader = FastaReader(self.temp_file.name)
        self.assertTrue(reader.is_fasta())

    def test_read_records(self):
        reader = FastaReader(self.temp_file.name)
        records = list(reader.read_records())
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0].header, "sequence1")
        self.assertEqual(records[1].header, "sequence2")


if __name__ == '__main__':
    unittest.main()