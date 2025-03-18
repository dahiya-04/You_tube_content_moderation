from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pytube import YouTube
import pandas as pd
from googleapiclient.discovery import build
from collections import Counter

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt_tab')

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('lstm_model_fina.h5')  # Update path if necessary

# Initialize the tokenizer
tokenizer = Tokenizer(num_words=1500)

# Preprocess text for text input
def preprocess_text_input(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [word for word in text if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    text = [lemmatizer.lemmatize(word) for word in text]
    return ' '.join(text)

# YouTube API setup (Replace with your own API Key)
API_KEY = "AIzaSyDAOgG9Wcok2I3eVMAsooubpUoVuz1zGL8"  
  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to extract and format YouTube metadata and comments
def get_video_data(video_url):
    yt = YouTube(video_url)
    video_id = yt.video_id
    title = yt.title
    description = yt.description
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    
    while request:
        response = request.execute()
        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        request = youtube.commentThreads().list_next(request, response)
    
    data = []
    for comment in comments:
        concatenated_text = f"{title} {description} {comment}"
        data.append({
            "video_id": video_id,
            "title": title,
            "description": description,
            "comment": comment,
            "text": concatenated_text
        })
    
    return pd.DataFrame(data)

# Function to preprocess text for prediction
def preprocess_text_youtube(texts, max_length=1000):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')
    return padded

# Function to make predictions and assign a final label
def predict_video_label(video_data):
    processed_texts = preprocess_text_youtube(video_data['text'].tolist())
    predictions = model.predict(processed_texts)
    predicted_labels = [np.argmax(pred) for pred in predictions]
    
    label_mapping = {0: 'Safe', 1: 'Harmful', 2: 'Neutral'}
    mapped_labels = [label_mapping[label] for label in predicted_labels]
    
    # Count occurrences of each label
    label_counts = Counter(mapped_labels)
    final_label = label_counts.most_common(1)[0][0]  # Get most frequent label
    
    return final_label, mapped_labels

@app.route('/analyze_video', methods=['POST'])
def analyze_video_route():
    url = request.form['video_url']
    video_data = get_video_data(url)
    final_label, comment_labels = predict_video_label(video_data)
    
    return jsonify({
        "video_id": video_data.iloc[0]['video_id'],
        "title": video_data.iloc[0]['title'],
        "description": video_data.iloc[0]['description'],
        "final_classification": final_label,
        "comment_classifications": comment_labels
    })

if __name__ == '__main__':
    app.run(debug=True)
