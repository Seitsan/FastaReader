from fasta_reader import FastaReader

def main():
    """
    Основной модуль демонстрационной программы
    """

    path = r"C:\Users\denko\Downloads\GCA_000006945.2_ASM694v2_genomic.fna"

    try:
        fasta_reader = FastaReader(path)

        if not fasta_reader.is_fasta():
            return 'Указанный файл не является файлом формата Fasta'

        for i, seq_record in enumerate(fasta_reader.read_records(), 1):
            print(f'Запись #{i}:')
            print(seq_record)
            print('-' * 50)

            if i >= 3:
                print('И так далее...')
                break


    except Exception as e:
        print(f'Произошла ошибка {e}')


if __name__ == "__main__":
    main()


