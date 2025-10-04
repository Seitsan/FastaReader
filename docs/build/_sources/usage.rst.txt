Использование
=============

Быстрый старт
-------------

Пример использования программы:

.. code-block:: python

   from fasta_reader import FastaReader
   from seq import Seq

   path = "example.fna"
   fasta_reader = FastaReader(path)

   if fasta_reader.is_fasta():
       for seq_record in fasta_reader.read_records():
           print(seq_record)

Классы
------

FastaReader
~~~~~~~~~~~

Класс для чтения FASTA файлов.

**Методы:**

- ``is_fasta()`` - проверяет формат файла
- ``read_records()`` - читает записи из файла

Seq
~~~

Класс для работы с последовательностями.

**Методы:**

- ``alphabet_validation()`` - определяет тип последовательности
- ``__len__()`` - возвращает длину последовательности
- ``__str__()`` - строковое представление