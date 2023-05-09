import os
import time
import torch
import librosa
import torchaudio
import pandas as pd
import soundfile as sf

SOURCE_DIR = '/Users/rudyh/Documents/Python/datasets/Bio-Akustik-Gajah'
DEST_DIR = '/Users/rudyh/Documents/Python/datasets/Bio-Akustik-Gajah/segmented-audio-data'
METADATA_FILE = '/Users/rudyh/Documents/Python/pytorch/codes/Riset-AI-SIKGM/metadata.csv'

def process_and_save_audio_segments(metadata_file=METADATA_FILE, input_audio_dir=SOURCE_DIR, output_audio_dir=DEST_DIR):
	"""
	Process and save audio segments based on the metadata file.

	Parameters:
		metadata_df (pandas.DataFrame): Metadata dataframe
		input_audio_dir (str): Path to the input audio directory
		output_audio_dir (str): Path to the output audio directory

	Returns:
		pandas.DataFrame: Metadata dataframe of the output audio segments
	"""
	metadata_df = pd.read_csv(metadata_file)
	output_metadata = []
	class_counts = {}

	for index, row in metadata_df.iterrows():
		# Extract metadata
		start_time = row['start_time']
		end_time = row['end_time']
		class_name = row['sound_type']
		filename = row['filename']

		# Load the audio file
		try:
			audio_file_path = os.path.join(input_audio_dir, filename)
			audio_data, sample_rate = librosa.load(audio_file_path)
		except Exception as e:
			print(f'Error while loading {audio_file_path}: {e}')
			continue

		# Convert start and end times to sample indices
		start_sample = librosa.time_to_samples(start_time, sr=sample_rate)
		end_sample = librosa.time_to_samples(end_time, sr=sample_rate)

		# Extract the audio segment
		audio_segment = audio_data[start_sample:end_sample]

		# Create output filename and path
		# The index value is sequential relative to the class, e.g. growl_0.wav, growl_1.wav, rumble_0.wav, rumble_1.wav, etc.
		if class_name not in class_counts:
			class_counts[class_name] = 0

		output_filename = f'{class_name}_{class_counts[class_name]}.wav'
		output_file_path = os.path.join(output_audio_dir, output_filename)
		# output_filename = f'{class_name}_{index}.wav'
		# output_file_path = os.path.join(output_audio_dir, output_filename)

		# Save the audio segment as WAV File
		# Use safer mechanism to save the audio segment
		try:
			sf.write(output_file_path, audio_segment, sample_rate)
			print(f'Saved {output_filename} to {DEST_DIR} successfully')
		except Exception as e:
			print(f'Error while saving {output_filename}: {e}')
		
		class_counts[class_name] += 1

		# Add the metadata to the list
		output_metadata.append({
			'filename': output_filename,
			'sound_type': class_name,
			'sample_rate': sample_rate,
		})

	# Convert the list to Pandas DataFrame
	output_metadata = pd.DataFrame(output_metadata)
	return output_metadata

def create_new_metadata(df, audio_dir):
	"""
	Create new metadata dataframe based on the output audio segments.

	Parameters:
		df (pandas.DataFrame): Metadata dataframe

	Returns:
		pandas.DataFrame: New metadata dataframe
	"""
	df['num_frames'] = df['filename'].apply(
		lambda x: torchaudio.info(os.path.join(audio_dir, x)).num_frames
	)

	df['num_channels'] = df['filename'].apply(
		lambda x: torchaudio.info(os.path.join(audio_dir, x)).num_channels
	)

	df['bits_per_sample'] = df['filename'].apply(
		lambda x: torchaudio.info(os.path.join(audio_dir, x)).bits_per_sample
	)

	df['encoding'] = df['filename'].apply(
		lambda x: torchaudio.info(os.path.join(audio_dir, x)).encoding
	)

	return df

def main():
	# Process and save audio segments
	print('Processing and saving audio segments...')
	
	# Create timer in seconds
	start_time = time.time()
	output_metadata = process_and_save_audio_segments()
	end_time = time.time()
	print(f'Elapsed time: {end_time - start_time} seconds')
	
	# Create new metadata
	new_metadata = create_new_metadata(df=output_metadata, audio_dir=DEST_DIR)

	# Save the new metadata
	new_metadata.to_csv(os.path.join(DEST_DIR, 'new_metadata.csv'), index=False)

if __name__ == '__main__':
	"""
	Missing files:
	- Olivedananaknya_Swift2_20211122_150000.wav
	- Olivedananaknya_Swift2_20211122_160000.wav
	"""
	main()