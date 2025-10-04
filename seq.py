class Seq:

    """
    Класс для представления биологических последовательностей.

    Attributes
    ----------
    header : str
        Заголовок FASTA записи
    sequence : str
        Биологическая последовательность (нуклеотидная или аминокислотная)

    Methods
    -------
    alphabet_validation()
        Определяет алфавит последовательности (белковый/нуклеотидный)
    __len__()
        Возвращает длину последовательности
    __str__()
        Возвращает строковое представление объекта
        """

    def __init__(self, header, sequence):

        """
        Parameters
        ----------
        header : str
            Заголовок из FASTA файла (строка после '>')
        sequence : str
            Биологическая последовательность
        """

        self.header = header.strip() if header else ''
        self.sequence = sequence


    def __len__(self):

        """
        Возвращает длину последовательности.

        Returns
        -------
        int
            Длина последовательности
        """

        return len(self.sequence)


    def alphabet_validation(self):

        """
        Определяет алфавит последовательности на основе уникальных символов.

        Returns
        -------
        str
            'белковый', 'ДНК', 'РНК', 'смешанный' или 'пустая'

        Notes
        -----
        Использует статистический анализ для определения типа последовательности
        на основе уникальных символов, характерных для каждого алфавита.
        """

        protein_alphabet = set("DEFHIKLMNPQRSTVWY*")
        nucleotide_alphabet = set("ACGTU")

        clean_sequence = ''.join(char for char in self.sequence.upper()
                                 if char.isalpha() or char == '*')

        if not clean_sequence:
            return "пустая"

        seq_chars = set(clean_sequence)

        unique_protein_chars = protein_alphabet - nucleotide_alphabet

        if any(char in unique_protein_chars for char in seq_chars):
            return 'белковый'
        elif seq_chars.issubset(nucleotide_alphabet):
            if 'U' in seq_chars and 'T' not in seq_chars:
                return 'РНК'
            else:
                return 'ДНК'
        else:
            return 'смешанный'


    def __str__(self):
        """
        Создает читаемое строковое представление объекта.

        Returns
        -------
        str
            Форматированная строка с информацией о последовательности
        """

        return f'''
Заголовок fasta: {self.header}
Длина последовательности: {len(self)}
Алфавит последовательности: {self.alphabet_validation()}
Первые 50 символов последовательности: {self.sequence[:50]}'''