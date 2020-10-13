# Code
This folder contains the code, trained models, and data used to generate explanations for each of the image, text, audio, and ECG domains. 

## Prerequisites
Install the required Python packages.
```Python
pip3 install -r requirements.txt
```

## Contents

### Data
Here's the Google Drive Link to the preprocessed data:
https://drive.google.com/drive/folders/1ZRWIeUHxGbKpqWkJ2HpiSLtmUyllfThf?usp=sharing

Download each of the folders there and place them in `data/`

### Explanations Code
Inside the `explanations_code/` folder, there are the Jupyter notebooks for generating explanations using each of the methods used for the study for each domain.

Note: The font file included is required for generating some of the explanations for the text dataset.

### Trained Models
Inside the `trained_models/` folder, there are the pretrained models used for the study, named as `[domain].hdf5` for each of the domains: image, text, audio, ECG.

### Training Code
Inside the `training_code/` folder, there are the Jupyter notebooks for training the models used during the study.
