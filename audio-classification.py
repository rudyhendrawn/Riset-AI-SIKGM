import tensorflow as tf
import tflite_model_maker as mm
from tflite_model_maker import audio_classifier
import os

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import glob
import random

from IPython.display import Audio, Image
from scipy.io import wavfile

print(f"TensorFlow Version: {tf.__version__}")
print(f"Model Maker Version: {mm.__version__}")

DATA_DIR = '/tf/segmented_audio_data_v2/'
MODEL_DIR = '/tf/model/'
TF_LITE_MODEL_DIR = '/tf/model/tflite-model/'

spec = audio_classifier.YamNetSpec(
	keep_yamnet_and_custom_heads=True,
	frame_step=1*audio_classifier.YamNetSpec.EXPECTED_WAVEFORM_LENGTH,
	frame_length=3*audio_classifier.YamNetSpec.EXPECTED_WAVEFORM_LENGTH)

train_data = audio_classifier.DataLoader.from_folder(spec, os.path.join(DATA_DIR, '/tf/segmented_audio_data_v2/train'), cache=True)
validation_data = audio_classifier.DataLoader.from_folder(spec, os.path.join(DATA_DIR, '/tf/segmented_audio_data_v2/val'), cache=True)
test_data = audio_classifier.DataLoader.from_folder(spec, os.path.join(DATA_DIR, '/tf/segmented_audio_data_v2/test'), cache=True)

batch_size = 2
epochs = 25

print('Training the model')
model = audio_classifier.create(
	train_data=train_data,
	model_spec=spec,
	validation_data=validation_data,
	batch_size=batch_size,
	epochs=epochs)

print('Evaluating the model')
model.evaluate(test_data)

# print(f'Exporting the TFLite model to {TF_LITE_MODEL_DIR}')
# try:
	# model.export(TF_LITE_MODEL_DIR, tflite_filename='Riset_AI_SIKGM_model_v0.1c.tflite')
	# model.export_tflite(
	# 	model,
	# 	os.path.join(TF_LITE_MODEL_DIR, 'Riset_AI_SIKGM_model_v0.1b.tflite'),
	# 	with_metadata=True,
	# 	export_metadata_json_file=True)
	# model.export(TF_LITE_MODEL_DIR, tflite_filename='Riset_AI_SIKGM_model_v0.1c.tflite', export_format=[mm.ExportFormat.SAVED_MODEL, mm.ExportFormat.LABEL])
# except Exception as e:
# 	print(e)