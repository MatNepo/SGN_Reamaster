# SGN_Reamaster
This is a remastered code of Semantics-Guided Neural Networks for 
Efficient Skeleton-Based Human Action Recognition (Microsoft) which was taken 
from [this](https://github.com/microsoft/SGN/tree/master) repository.

# Dependencies

## 1. Create virtual env:
```bash
python -m venv venv
```

## 2. Download CUDA
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## 3. Install requirements
#### Check versions of Python and PyTorch
```
Python >= 3.6
PyTorch >= 1.10.0
```
#### Before installing check versions in the same named .txt file
```bash
pip install -r requirements.txt
```

### Download datasets.

#### There are 3 datasets to download:

- NTU RGB+D 60 Skeleton
- NTU RGB+D 120 Skeleton
- NW-UCLA

#### NTU RGB+D 60 and 120

1. Request dataset here: https://rose1.ntu.edu.sg/dataset/actionRecognition
2. Download the skeleton-only datasets:
   1. `nturgbd_skeletons_s001_to_s017.zip` (NTU RGB+D 60)
   2. `nturgbd_skeletons_s018_to_s032.zip` (NTU RGB+D 120)
   3. Extract above files to `./data/nturgbd_raw`

#### NW-UCLA

1. Download dataset from here: https://www.dropbox.com/s/10pcm4pksjy6mkq/all_sqe.zip?dl=0
2. Move `all_sqe` to `./data/NW-UCLA`

# Data Preparation

## Data Preparation Scripts

This repository contains four Python scripts used for data preparation:

1. #### **script_0_to_copy.py**: 
   Copies files from one directory to another using multi-threading for 
improved performance.

2. #### **script_1_copy_logs.py**: 
   Creates a reduced dataset by filtering and copying files based on 
specific criteria (e.g., file size, action numbers). It also generates 
a log of non-copied files.

3. #### **script_2_skes_creator.py**: 
   Generates a 'skes_available_name.txt' file containing a list of 
skeleton file names without extensions, which is used in subsequent 
processing steps.

4. #### **script_3_txt_files_creator.py**: 
   Processes the `skes_available_name.txt` file to extract specific 
information (`setup`, `camera`, `performer`, `replication` and action 
class `label`) from each filename and writes this data into separate 
output files.

These scripts are designed to prepare and organize data for the SGN 
(Semantics-Guided Neural Networks) project, facilitating efficient data 
handling and preprocessing.

## Run scripts

Before running scripts 1 and 3 don't forget to change paths:

#### **script_1_copy_logs.py**

Change `dataset_path` on `69` line

```bash
   python script_1_skes_creator.py
```

![image](https://github.com/MatNepo/SGN_Reamaster/blob/main/images/skript_1_1.png)
![image](https://github.com/MatNepo/SGN_Reamaster/blob/main/images/skript_1_2.png)

#### **script_2_skes_creator.py**

Change `dataset_path` on the 12th line and run the code. It creates `skes_available_name.txt` file 
in `./data/ntu/statistics` directory.

```bash
   python script_2_skes_creator.py
```

If you decided to change the size, don't forget to change the amount of files in the dataset in 
`3_seq_transformation.py` file on the 132 line:

```python
   labels_vector = np.zeros((num_skes, 60))  # 60 is an amount of actions/labels inside the dataset
```

![image](https://github.com/MatNepo/SGN_Reamaster/blob/main/images/skript_2_1.png)
![image](https://github.com/MatNepo/SGN_Reamaster/blob/main/images/skript_2_2.png)

#### **script_3_txt_files_creator.py**

Change absolute paths for `INPU_DIR` and `OUTPUT_DIR` on lines `20-21`

```bash
   python script_3_txt_files_creator.py
```

[image]()
[image]()

## Process the data

To find the code below go to the dir: `.\data\ntu`. Here you'll find 3 scripts to process the data

#### **1_get_raw_skes_data.py**

Change `skes_path` on `140` line (path to the new one dataset which was created above)

```bash
   python 1_get_raw_skes_data.py
```

#### **2_get_raw_denoised_data.py**

Just run the code

```bash
   python 2_get_raw_denoised_data.py
```

#### **3_seq_transformation.py**

Just run the code

```bash
   python 3_seq_transformation.py
```

# Training

```bash
# For the CS setting
python  main.py --network SGN --train 1 --case 0
# For the CV setting
python  main.py --network SGN --train 1 --case 1
```

# Testing

- Test the pre-trained models (./results/NTU/SGN/)
```bash
# For the CS setting
python  main.py --network SGN --train 0 --case 0
# For the CV setting
python  main.py --network SGN --train 0 --case 1
```