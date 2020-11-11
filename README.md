# How Can I Explain This to You? An Empirical Study of Deep Neural Network Explanation Methods [NeurIPS 2020]
This repository is the official implementation and it contains the code, trained models, and data used to generate explanations for each of the image, text, audio, and ECG domains. 

## Prerequisites
Install the required Python packages.
```Python
pip3 install -r requirements.txt
```

## Contents

### Data
Here's the Google Drive Link to the preprocessed data: [Link](https://drive.google.com/drive/folders/1ZRWIeUHxGbKpqWkJ2HpiSLtmUyllfThf?usp=sharing)

Download each of the folders there and place them in `data/`

### Training Code
Inside the `training_code/` folder, there are the Jupyter notebooks for training the models used during the study.

### Trained Models
Inside the `trained_models/` folder, there are the pretrained models used for the study, named as `[domain].hdf5` for each of the domains: image, text, audio, ECG.

### Explanations Code
Inside the `explanations_code/` folder, there are the Jupyter notebooks for generating explanations using each of the methods used for the study for each domain.

Note: The font file included is required for generating some of the explanations for the text dataset.

<img src="images/Explanations.png" alt="Explanations">

### Survey Responses
Inside the `survey responses/` folder, we have the survey responses collected from the Amazon Turk Study and the code to process them.

## Results from the AMT Study

The values indicate the rate by which users selected a particular method when it is an available explanation, with 95% bootstrap confidence intervals

<img src="images/Results.JPG" alt="Results">

## BibTex

If you find this code and results useful in your research, please cite:

	@article{jeyakumar2020can,
	  title={How Can I Explain This to You? An Empirical Study of Deep Neural Network Explanation Methods},
	  author={Jeyakumar, Jeya Vikranth and Noor, Joseph and Cheng, Yu-Hsi and Garcia, Luis and Srivastava, Mani},
	  journal={Advances in Neural Information Processing Systems},
	  volume={33},
	  year={2020}
	}