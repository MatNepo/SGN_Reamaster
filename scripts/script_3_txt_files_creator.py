"""
    This script processes a list of filenames from an input file, extracts specific numbers from each filename,
    and writes these numbers to separate output files. The filenames are expected to be in the format
    'S___C___P___R___A___', where '_' represents digits. The script extracts the following information:

        - Setup number (S)
        - Camera ID (C)
        - Performer ID (P)
        - Replication number (R)
        - Action class label (A)

    Each type of information is written to a separate output file, maintaining the order of the input filenames.
"""


import re
import os

# Пути к файлам
INPUT_FILE = r"/data/ntu/statistics/skes_available_name.txt"
OUTPUT_DIR = r"/data/ntu/statistics"

# Массив с названиями выходных файлов
FILES = ['setup', 'camera', 'performer', 'replication', 'label']

# Создаем словарь с полными путями к выходным файлам
OUTPUT_FILES = {file: os.path.join(OUTPUT_DIR, f"{file}.txt") for file in FILES}


def extract_numbers(filename):
    """Извлекает числа из имени файла."""
    pattern = r'S(\d+)C(\d+)P(\d+)R(\d+)A(\d+)'
    match = re.match(pattern, filename)
    if match:
        setup = int(match.group(1))
        camera = int(match.group(2))
        performer = int(match.group(3))
        replication = int(match.group(4))
        action = int(match.group(5))
        return [setup, camera, performer, replication, action]
    raise ValueError(f"Неверный формат имени файла: {filename}")


def process_data(input_file, output_files):
    """Обрабатывает входной файл и записывает результаты."""
    output_data = {key: [] for key in FILES}

    with open(input_file, 'r') as f:
        for filename in f:
            filename = filename.strip()
            try:
                numbers = extract_numbers(filename)
                for i, file in enumerate(FILES):
                    output_data[file].append(str(numbers[i]))
            except ValueError as e:
                print(f"Ошибка: {e}")

    for file in FILES:
        with open(output_files[file], 'w') as f:
            f.write('\n'.join(output_data[file]))


def main():
    """Основная функция скрипта."""
    print("Начало обработки данных...")
    process_data(INPUT_FILE, OUTPUT_FILES)
    print("Обработка данных успешно завершена.")


if __name__ == "__main__":
    main()
