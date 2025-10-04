import os
from seq import Seq

class FastaReader:

    """
        Класс для чтения и обработки файлов в формате FASTA.

        Attributes
        ----------
        path_to_fasta : str
            Путь к FASTA файлу

        Methods
        -------
        is_fasta()
            Проверяет, является ли файл корректным FASTA файлом

        read_records()
            Читает все записи из FASTA файла и возвращает генератор объектов Seq
        """

    def __init__(self, path_to_fasta):

        """
        Parameters
        ----------
        path_to_fasta : str
            Путь к FASTA файлу для чтения
        """

        self.path_to_fasta = path_to_fasta


    def is_fasta(self):

        """
        Проверяет соответствие файла формату FASTA по расширению и содержимому.

        Returns
        -------
        bool
            True если файл соответствует формату FASTA, иначе False

        Examples
        --------
        >>> reader = FastaReader("example.fna")
        >>> reader.is_fasta()
        True
        """

        valid_extensions = ('.fasta', '.fna', '.fa', '.faa', '.ffn', '.frn')
        if not self.path_to_fasta.lower().endswith(valid_extensions):
            return False

        if not os.path.exists(self.path_to_fasta):
            return False

        try:
            with open(self.path_to_fasta, 'r') as file:
                first_line = file.readline().strip()
                return first_line.startswith('>')
        except (IOError, UnicodeDecodeError):
            return False


    def read_records(self):

        """
        Читает FASTA файл построчно и возвращает объекты Seq.

        Yields
        ------
        Seq
            Объекты последовательности из FASTA файла

        Raises
        ------
        ValueError
            Если файл не является корректным FASTA файлом

        Examples
        --------
        >>> reader = FastaReader("example.fna")
        >>> for record in reader.read_records():
        ...     print(record)
        """

        if not self.is_fasta():
            raise ValueError(f"Файл {self.path_to_fasta} не является корректным FASTA файлом")

        current_header = None
        current_sequence = []

        with open(self.path_to_fasta, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith('>'):
                    if current_header is not None:
                        yield Seq(current_header, ''.join(current_sequence))

                    current_header = line[1:] #Чтобы убрать '>'
                    current_sequence = []
                else:
                    current_sequence.append(line)

            if current_header is not None:
                yield Seq(current_header, ''.join(current_sequence))