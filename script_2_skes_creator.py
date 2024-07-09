"""
    Just creates skes_available_name.txt file

    - Выполняется перед компиляцией файла get_raw_skes.py
"""

import os


def main():
    # Путь к датасету, из которого будут считываться данные
    dataset_path = r"D:\Users\Legion\BIA Technologies\dataset_SGN"  # folder with datasets
    skes_path = os.path.join(dataset_path, 'raw_txt_mini')
    # skes_path = 'D:/Users/Legion/BIA Technologies/dataset_SGN/raw_txt'

    # Путь, где будет создан файл skes_available_name.txt
    output_path = './data/ntu/statistics'  # Измените этот путь на нужный

    # Получаем список всех файлов в директории skes_path
    files = os.listdir(skes_path)

    # Полный путь к создаваемому файлу
    output_file = os.path.join(output_path, r'skes_available_name.txt')

    # Открываем (или создаем) файл skes_available_name.txt для записи
    with open(output_file, 'w') as f:
        for i, file in enumerate(files):
            # Получаем имя файла без расширения
            name_without_extension = os.path.splitext(file)[0]
            # Добавляем перевод строки только если это не последний файл
            if i < len(files) - 1:
                f.write(name_without_extension + '\n')
            else:
                f.write(name_without_extension)

    print(f"Файл skes_available_name.txt создан в {output_path} и заполнен именами файлов.")


if __name__ == '__main__':
    main()
