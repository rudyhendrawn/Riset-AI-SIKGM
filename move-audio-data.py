"""
To use this script, you need to have the following directory structure:
	1. A directory containing all the audio files as source directory
	2. A destination directory containing the following subdirectories:
		- train
		- val
		- test
		- train.csv
		- val.csv
		- test.csv
	3. In each of the train, val, and test subdirectories, there should be label/class subdirectories
"""

import os
import pandas as pd
import shutil

SOURCE_DIR = 'your-source-directory'
DEST_DIR = 'your-destination-directory'
DEST_TRAIN_DIR = os.path.join(DEST_DIR, 'train')
DEST_VALIDATION_DIR = os.path.join(DEST_DIR, 'val')
DEST_TEST_DIR = os.path.join(DEST_DIR, 'test')

"""
Create directory if not exists
"""
def create_dir_if_not_exists(dir_path: str, class_dir: list):
	for cls in class_dir:
		new_dir = os.path.join(dir_path, cls)
		if not os.path.exists(new_dir):
			os.makedirs(new_dir)

"""
Move file to destination directory
"""
def move_file_to_class(dataframe, source_dir: str, destination_dir: str):
	for index, row in dataframe.iterrows():
		source_path = os.path.join(source_dir, row['filename'])
		destination_path = os.path.join(destination_dir, row['sound_type'], row['filename'])
		try:
			shutil.move(source_path, destination_path)
			print(f"Move {source_path} to {destination_path}")
		except shutil.Error as e:
			print(f"An error occurred: {e}")

"""
Copy file to destination directory
"""
def copy_file_to_class(dataframe, source_dir: str, destination_dir: str):
	for index, row in dataframe.iterrows():
		source_path = os.path.join(source_dir, row['filename'])
		destination_path = os.path.join(destination_dir, row['sound_type'], row['filename'])
		try:
			shutil.copy(source_path, destination_path)
			print(f"Copy {source_path} to {destination_path}")
		except shutil.Error as e:
			print(f"An error occurred: {e}")

train_metadata = pd.read_csv(os.path.join(DEST_DIR, 'train.csv'))
val_metadata = pd.read_csv(os.path.join(DEST_DIR, 'val.csv'))
test_metadata = pd.read_csv(os.path.join(DEST_DIR, 'test.csv'))

copy_file_to_class(train_metadata, SOURCE_DIR, DEST_TRAIN_DIR)
copy_file_to_class(val_metadata, SOURCE_DIR, DEST_VALIDATION_DIR)
copy_file_to_class(test_metadata, SOURCE_DIR, DEST_TEST_DIR)

# # Give complete path to filename
# train_metadata['filename'] = train_metadata['filename'].apply(lambda x: os.path.join(DATA_DIR, 'train', x))
# val_metadata['filename'] = val_metadata['filename'].apply(lambda x: os.path.join(DATA_DIR, 'val', x))
# test_metadata['filename'] = test_metadata['filename'].apply(lambda x: os.path.join(DATA_DIR, 'test', x))

# class_list = train_metadata['alt_class'].unique()
# cls_ls = ['other', 'roar', 'rumble', 'growl', 'trumpet', 'roar_rumble', 'bark_rumble', 'bark']

# move_file_to_class(train_metadata, TRAIN_DIR)
# move_file_to_class(val_metadata, VALIDATION_DIR)
# move_file_to_class(test_metadata, TEST_DIR)


# for fpath in val_metadata['filename']:
# 	move_file(fpath, os.path.join(DATA_DIR, 'val'))

# for fpath in test_metadata['filename']:
# 	move_file(fpath, os.path.join(DATA_DIR, 'test'))