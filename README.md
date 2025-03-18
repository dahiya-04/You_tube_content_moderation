# README: Sentiment Analysis Pipeline

## Overview
This project involves sentiment analysis on textual data, specifically YouTube video metadata and comments. It leverages a pre-trained model from Hugging Face and an LSTM model for sentiment classification. The notebook preprocesses text data before performing classification.

## Installation
To run this notebook and the Flask application, ensure you have the necessary dependencies installed:
```bash
pip install python-dotenv googleapiclient transformers torch tensorflow keras flask nltk pytube
```

## Steps in the Notebook

### 1. Environment Setup
- The script initializes required libraries and environment variables.
- It installs necessary dependencies like `python-dotenv` to handle API credentials.

### 2. Data Retrieval
- The Google API Client and Pytube are used to fetch data from YouTube.
- Authentication is handled via environment variables to access APIs securely.
- The script extracts video metadata (title, description) and comments for analysis.

### 3. Data Preprocessing
- The text data is cleaned, tokenized, and prepared for sentiment analysis.
- Steps include:
  - Converting text to lowercase
  - Removing stopwords
  - Tokenization
  - Lemmatization
  - Padding sequences for LSTM input

### 4. Sentiment Analysis
- Two models are used for sentiment classification:
  1. A pre-trained transformer model from Hugging Face.
  2. A custom-trained LSTM model for sentiment analysis.
- The `pipeline` class is used for transformer-based predictions.
- The LSTM model is loaded from `lstm_model_fina.h5` and used for classification.
- The text data (title, description, and comments) is tokenized and padded before passing it to the LSTM model.
- The model categorizes sentiment into Safe, Harmful, or Neutral.

### 5. Flask API for Sentiment Analysis
- A Flask application (`app.py`) provides an endpoint to analyze YouTube videos.
- The `/analyze_video` endpoint:
  - Accepts a YouTube video URL.
  - Extracts metadata and comments.
  - Processes text and applies sentiment classification using the LSTM model.
  - Returns a JSON response with classification results.

### 6. How Sentiment Classification Works in the API
- The API receives a YouTube video URL via a POST request.
- It extracts the video’s metadata and comments.
- The text (title, description, and comments) is preprocessed (tokenized, lemmatized, and padded).
- The processed text is passed through the LSTM model for classification.
- The model assigns each text snippet a sentiment label (Safe, Harmful, or Neutral).
- The sentiment of the entire video is determined based on the most common label among the comments.
- The API returns a JSON response containing:
  - The video ID, title, and description.
  - The final sentiment classification.
  - Individual classifications for each comment.

### 7. Output Analysis
- The classified sentiments are stored or visualized for further analysis.
- Results from both models can be compared to evaluate performance.

![image](https://github.com/user-attachments/assets/746d851e-fc4b-4102-91d6-f713afd4feea)


## Usage
1. Run the Jupyter Notebook cell by cell to execute the sentiment analysis pipeline.
2. To start the Flask API, run:
   ```bash
   python app.py
   ```
3. Send a POST request to the `/analyze_video` endpoint with a YouTube video URL.

## Future Improvements
- Fine-tuning the sentiment model on a custom dataset.
- Expanding preprocessing steps for better accuracy.
- Integrating more advanced visualization techniques.
- Optimizing the LSTM model for improved performance.
- Enhancing the Flask API with additional endpoints for detailed analysis.


