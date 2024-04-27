## Project Title: Elephant Vocal Classification Using Deep Learning

### Overview
This project focuses on the innovative use of deep learning to classify elephant vocalizations, aiming to contribute to wildlife conservation efforts and the study of elephant communication. By accurately identifying different elephant calls, such as `roar`, `rumble`, `growl`, `trumpet`, `roar_rumble`, `bark_rumble`, `bark`, and `other`, the model provides valuable insights into elephant behavior and social dynamics.

### Technologies Used
- Tensorflow: An open-source machine learning framework for building and training deep learning models.
- Yamnet: A pre-trained deep learning model used to analyze audio signals.
- Android: Platform for deploying the inference model to make the technology accessible in mobile applications (out of this repository scope).

### Project Description
The primary goal of this project was to leverage the power of machine learning to classify various elephant vocalizations into categories including roars, rumbles, growls, trumpets, roar-rumbles, bark-rumbles, barks, and other vocal types. Utilizing Yamnet, a sophisticated pre-trained model known for its efficiency in audio processing, served as the foundation for feature extraction.

#### The project involved several key phases

- **Data Collection**
The raw audio data is provided by the elephant researchers using sensors and audio recorder. They carefully curated and labeled to ensure accurate classification of vocalizations using ELOC (Elephant Listening Observation and Conservation) device. In each raw audio data file, the researchers identified the start and end times of each vocalization, along with the corresponding vocal type.

- **Data Preprocessing**
Extracted audio segment from the raw data based on start and end times of each vocalization. The audio segments were then converted into small audio wav files labeled with the corresponding vocal type. In this phase also, the metadata were created to store the sample rate, number of frames, number of channels, bits per sample, encoding, and class label.

- **Modeling** 
Yamnet model was used to extract audio features from the preprocessed audio data and also as a classifier to predict the vocal type of each audio segment. In this phase, I kept the Yamnet and custom heads to be trained together to improve the model's performance.

- **Deployment**
The trained model was successfully exported and integrated into an Android application, allowing for real-time audio classification in a mobile environment.

#### Results
The model demonstrated a bias accuracy in classifying elephant vocalizations. It was caused by the imbalanced and limited dataset, which affected the model's ability to generalize across different vocal types.

### Challenges and Learnings
One of the main challenges faced during the project was the limited availability of labeled elephant vocalization data. This led to an imbalanced dataset, which affected the model's performance and generalization. To address this issue, future work will focus on collecting more diverse and extensive datasets to improve the model's accuracy and robustness.

### Acknowledgments
I would like to express my gratitude to the elephant researchers and conservationists from Fakultas Kehutanan Universitas Gadjah Mada, Yogyakarta, Indonesia, and [International Elephant Project (IEP)](https://www.internationalelephantproject.org/what-we-do/), who provided the valuable audio data for this project. Their dedication and efforts in studying and protecting elephants have made this research possible. 

