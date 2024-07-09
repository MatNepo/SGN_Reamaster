"""
    Script just to copy files from one directory to another
"""

import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed


def copy_file(src_file, dest_dir):
    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
    shutil.copy2(src_file, dest_file)
    return src_file


def copy_files(src_dir, dest_dir, num_threads=8):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(copy_file, file, dest_dir) for file in files]
        for future in as_completed(futures):
            try:
                file = future.result()
                print('Copied file: {}'.format(file))
            except Exception as e:
                print('Error copying file: {}'.format(e))


if __name__ == '__main__':
    source_directory = r'D:\Users\Legion\BIA Technologies\dataset_SGN\raw_txt'
    destination_directory = r'D:\Users\Legion\BIA Technologies\HD-GCN-main\data\ntu\nturgb+d_skeletons'
    copy_files(source_directory, destination_directory)
