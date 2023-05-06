import os
import torch
import librosa
import torchaudio
import pandas as pd
import soundfile as sf

SOURCE_DIR = '/Users/rudyh/Documents/Python/datasets/Bio-Akustik-Gajah'
DEST_DIR = '/Users/rudyh/Documents/Python/datasets/Bio-Akustik-Gajah/segmented-audio-data'
METADATA_FILE = 'codes/Riset-AI-SIKGM/metadata.csv'

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

	for index, row in metadata_df.iterrows():
		# Extract metadata
		start_time = row['start_time']
		end_time = row['end_time']
		class_name = row['sound_type']
		filename = row['filename']

		# Load the audio file
		audio_file_path = os.path.join(input_audio_dir, filename)
		audio_data, sample_rate = librosa.load(audio_file_path)

		# Convert start and end times to sample indices
		start_sample = librosa.time_to_samples(start_time, sr=sample_rate)
		end_sample = librosa.time_to_samples(end_time, sr=sample_rate)

		# Extract the audio segment
		audio_segment = audio_data[start_sample:end_sample]

		# Create output filename and path
		output_filename = f'{class_name}_{index}.wav'
		output_file_path = os.path.join(output_audio_dir, output_filename)

		# Save the audio segment as WAV File
		sf.write(output_file_path, audio_segment, sample_rate)

		# Add the metadata to the list
		output_metadata.append({
			'filename': output_filename,
			'sound_type': class_name,
			'sample_rate': sample_rate,
		})

	# Convert the list to Pandas DataFrame
	output_metadata = pd.DataFrame(output_metadata)
	return output_metadata

def create_new_metadata(df=metadata_df, audio_dir=DEST_DIR):
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