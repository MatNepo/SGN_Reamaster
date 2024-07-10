"""
    Создание нового уменьшенного датасета (без файлов с 0-ми скелетонами и с возможным заданием кол-ва actions)

    - Изменение размера датасета путём удаления файлов, в названии которых
      в части *A0001.skeleton содержится число > 30
"""

# Изменение размера датасета путём удаления файлов, в названии которых в части *A0001.skeleton содержится число > 30

import os
import shutil
import concurrent.futures
import time


def tree2list(directory):
    """
    Генератор, который обходит все файлы в указанной директории.

    :param directory: Строка, путь к исходной директории
    :return: Генератор, возвращающий пути к файлам
    """
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


def filter_files(files, files_in_dataset):
    """
    Фильтрует файлы на те, которые нужно копировать и те, которые не удовлетворяют условиям.

    :param files: Список строк, пути к файлам
    :return: Кортеж из трех элементов:
             - Список путей к файлам, которые нужно скопировать
             - Список номеров файлов, которые не нужно копировать
             - Количество файлов размером менее 1024 байт
    """
    to_copy = []
    not_to_copy = []
    small_files_count = 0
    for file_path in files:
        file_name = os.path.basename(file_path)
        file_size = os.stat(file_path).st_size
        if file_size < 1024:
            small_files_count += 1
        if file_name.endswith(".skeleton"):
            try:
                file_number = int(file_name.split('A')[1].split('.')[0])
                if 1 <= file_number <= files_in_dataset and file_size > 1024:
                    to_copy.append(file_path)
                else:
                    not_to_copy.append(file_path)
            except ValueError:
                continue
    return to_copy, not_to_copy, small_files_count


def copy_file(source_file_path, destination_folder):
    """
    Копирует файл в целевую директорию.

    :param source_file_path: Строка, путь к исходному файлу
    :param destination_folder: Строка, путь к целевой директории
    """
    destination_file_path = os.path.join(destination_folder, os.path.basename(source_file_path))
    shutil.copy2(source_file_path, destination_file_path)


dataset_path = r"D:\Users\Legion\BIA Technologies\dataset_SGN"  # folder with datasets
source_folder = os.path.join(dataset_path, r'raw_txt')  # original dataset with 60 actions path
destination_folder = os.path.join(dataset_path, r'raw_txt_mini')  # new dataset created from the original one
log_file_path = os.path.join(dataset_path, r'non_copied_files.txt')  # non-copied files from original to new dataset

if __name__ == '__main__':
    start_time = time.time()  # Засекаем время начала выполнения скрипта

    # Создание целевой директории, если она не существует
    os.makedirs(destination_folder, exist_ok=True)

    # Получение всех файлов с помощью tree2list
    all_files = list(tree2list(source_folder))

    # Сортировка всех файлов по имени
    all_files.sort()

    # Фильтрация файлов
    files_to_copy, files_not_to_copy, small_files_count = filter_files(all_files, files_in_dataset=30)

    # Определение порядковых номеров файлов, которые не будут скопированы
    files_not_to_copy_indices = [all_files.index(file) + 1 for file in files_not_to_copy]

    # Параллельное копирование файлов
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(copy_file, file_path, destination_folder) for file_path in files_to_copy]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Ошибка при копировании файла: {e}")

    end_time = time.time()  # Засекаем время окончания выполнения скрипта
    execution_time = end_time - start_time  # Вычисляем время выполнения

    # Запись номеров не скопированных файлов
    with open(log_file_path, 'w') as log_file:
        for file_index in files_not_to_copy_indices:
            log_file.write(f'{file_index}\n')

    # Вывод информации о выполнении скрипта
    print("Копирование завершено.")
    print(f"Файлы скопированы в директорию: {destination_folder}.")
    print(f"Файлы, которые не были скопированы, записаны в {log_file_path}.")
    print(f"Время выполнения скрипта: {execution_time:.2f} секунд.")
    print(f"Количество файлов, скопированных: {len(files_to_copy)}")
    print(f"Количество файлов, не скопированных: {len(files_not_to_copy)}")
    print(f"Количество файлов в исходной директории размером менее 1024 байт: {small_files_count}")
