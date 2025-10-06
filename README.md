# FastaReader

Python библиотека для чтения и анализа файлов в формате FASTA.

## Возможности

- Чтение FASTA файлов любого размера
- Автоматическое определение типа последовательности (ДНК/РНК/белковая)
- Получение информации о последовательностях
- Валидация формата FASTA файлов

## Установка

```bash

# Клонируйте репозиторий
git clone https://github.com/Seitsan/FastaReader.git
cd FastaReader
```

## Быстрый старт

```python
from fasta_reader import FastaReader

# Создайте объект для чтения FASTA файла
reader = FastaReader("example.fna")

# Проверьте формат файла
if reader.is_fasta():
    # Читайте записи последовательностей
    for i, seq_record in enumerate(reader.read_records(), 1):
        print(f"Запись #{i}:")
        print(seq_record)
        print("-" * 50)
else:
    print("Файл не является корректным FASTA файлом")
```

## Пример вывода
```text
Запись #1:
Заголовок fasta: sequence_1 description
Длина последовательности: 150
Алфавит последовательности: ДНК
Первые 50 символов последовательности: ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA

--------------------------------------------------
```

## Структура проекта

```text
FastaReader/
├── fasta_reader.py  # Основной класс для чтения FASTA
├── seq.py           # Класс для работы с последовательностями
├── main.py          # Пример использования
├── docs/            # Документация
├── tests/           # Тесты
└── examples/        # Примеры файлов
```

## Документация
Полная документация доступна в папке `docs/`

## Разработка

### Запуск тестов

```bash

python -m pytest tests/
```

### Сборка документации

```bash

cd docs
sphinx-build -b html source build   #Лучше использовать для Windows
```

## Лицензия
Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.

## Вклад в проект
1. Форкните репозиторий
2. Создайте ветку для новой функциональности (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add some amazing feature'`)
4. Запушьте в ветку (`git push origin feature/amazing-feature`)
5. Создайте Pull Request
