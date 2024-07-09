"""
    Old version of 3rd script
"""


import os


def read_lines_to_remove(non_copied_file_path):
    """
    Читает номера строк для удаления из указанного файла.

    :param non_copied_file_path: Строка, путь к файлу с номерами строк для удаления
    :return: Множество номеров строк для удаления
    """
    lines_to_remove = set()
    with open(non_copied_file_path, 'r') as non_copied_file:
        for line in non_copied_file:
            line = line.strip()
            if line.isdigit():
                lines_to_remove.add(int(line))
    return lines_to_remove


def copy_lines(source_file_path, destination_file_path, lines_to_remove):
    """
    Копирует строки из исходного файла в целевой файл, исключая указанные номера строк.

    :param source_file_path: Строка, путь к исходному файлу
    :param destination_file_path: Строка, путь к целевому файлу
    :param lines_to_remove: Множество номеров строк для удаления
    """
    with open(source_file_path, 'r', encoding='utf-8') as source_file, \
            open(destination_file_path, 'w', encoding='utf-8') as destination_file:
        lines = source_file.readlines()
        filtered_lines = [line.rstrip('\n') for index, line in enumerate(lines, start=1) if
                          index not in lines_to_remove]

        if filtered_lines:
            destination_file.write('\n'.join(filtered_lines))


def process_files(non_copied_file_path, source_file_paths, destination_file_paths):
    """
    Обрабатывает файлы, копируя строки из исходных файлов в целевые файлы, исключая указанные номера строк.

    :param non_copied_file_path: Строка, путь к файлу с номерами строк для удаления
    :param source_file_paths: Список строк, пути к исходным файлам
    :param destination_file_paths: Список строк, пути к целевым файлам
    """
    # Чтение номеров строк для удаления
    lines_to_remove = read_lines_to_remove(non_copied_file_path)

    # Копирование строк для каждой пары файлов
    for source_file_path, destination_file_path in zip(source_file_paths, destination_file_paths):
        copy_lines(source_file_path, destination_file_path, lines_to_remove)
        print(f"Копирование строк из файла {source_file_path} в {destination_file_path} завершено.")


def main():
    """
    Основная функция выполнения копирования строк из файлов *_old.txt в *.txt,
    исключая строки с номерами из non_copied_files.txt.
    """
    # Пути к файлам
    dataset_path = r'D:\Users\Legion\BIA Technologies\dataset_SGN'
    project_path = os.path.dirname(os.path.abspath(__file__))
    statistics_path = os.path.join(project_path, r'data\ntu\statistics')
    non_copied_file_path = os.path.join(dataset_path, 'non_copied_files.txt')

    # Исходные и целевые файлы
    files = ['performer', 'camera', 'label', 'replication', 'setup']
    source_file_paths = [os.path.join(statistics_path, f'{file}_old.txt') for file in files]
    destination_file_paths = [os.path.join(statistics_path, f'{file}.txt') for file in files]

    # Обработка файлов
    process_files(non_copied_file_path, source_file_paths, destination_file_paths)


if __name__ == "__main__":
    main()
