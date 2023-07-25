import os
import pandas as pd
import shutil

DATA_DIR = '/tf/segmented_audio_data_v2/'
TRAIN_DIR = '/tf/segmented_audio_data_v2/train'
VALIDATION_DIR = '/tf/segmented_audio_data_v2/val'
TEST_DIR = '/tf/segmented_audio_data_v2/test'

def move_file(file_path, destination_path):
	try:
		# shutil.move(file_path, destination_path)
		print(f"Moved {file_path} to {destination_path}")
	except shutil.Error as e:
		print(f"An error occurred: {e}")

def move_file_to_class(dataframe, data_dir):
	for index, row in dataframe.iterrows():
		file_path = os.path.join(data_dir, row['filename'])
		destination_path = os.path.join(data_dir, row['alt_class'], row['filename'])
		try:
			shutil.move(file_path, destination_path)
			print(f"Moved {file_path} to {destination_path}")
		except shutil.Error as e:
			print(f"An error occurred: {e}")

train_metadata = pd.read_csv(os.path.join(DATA_DIR, 'train.csv'))
val_metadata = pd.read_csv(os.path.join(DATA_DIR, 'val.csv'))
test_metadata = pd.read_csv(os.path.join(DATA_DIR, 'test.csv'))

# # Give complete path to filename
# train_metadata['filename'] = train_metadata['filename'].apply(lambda x: os.path.join(DATA_DIR, 'train', x))
# val_metadata['filename'] = val_metadata['filename'].apply(lambda x: os.path.join(DATA_DIR, 'val', x))
# test_metadata['filename'] = test_metadata['filename'].apply(lambda x: os.path.join(DATA_DIR, 'test', x))

# class_list = train_metadata['alt_class'].unique()
# cls_ls = ['other', 'roar', 'rumble', 'growl', 'trumpet', 'roar_rumble', 'bark_rumble', 'bark']

move_file_to_class(train_metadata, TRAIN_DIR)
move_file_to_class(val_metadata, VALIDATION_DIR)
move_file_to_class(test_metadata, TEST_DIR)


# for fpath in val_metadata['filename']:
# 	move_file(fpath, os.path.join(DATA_DIR, 'val'))

# for fpath in test_metadata['filename']:
# 	move_file(fpath, os.path.join(DATA_DIR, 'test'))