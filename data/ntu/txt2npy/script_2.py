import os
import shutil


def tree2list(directory):
    for entry in os.scandir(directory):
        if entry.is_dir():
            yield from tree2list(entry.path)
        else:
            yield entry


source_folder = r'D:\Users\Legion\BIA Technologies\dataset_SGN\raw_txt'
destination_folder = r'D:\Users\Legion\BIA Technologies\dataset_SGN\raw_txt_mini'

# Создание целевой директории, если она не существует
os.makedirs(destination_folder, exist_ok=True)

# Получение всех файлов с помощью tree2list и применение фильтрации через list comprehension
files_to_copy = [
    entry.path for entry in tree2list(source_folder)
    if entry.name.endswith(".skeleton")  # Фильтр по расширению файла
    and 1 <= int(entry.name.split('A')[1].split('.')[0]) <= 30  # Фильтр по номеру "A" от 1 до 30
]

# Копирование выбранных файлов
for source_file_path in files_to_copy:
    destination_file_path = os.path.join(destination_folder, os.path.basename(source_file_path))
    shutil.copy2(source_file_path, destination_file_path)
    print(f'Скопирован файл: {source_file_path} -> {destination_file_path}')

print("Копирование завершено.")
