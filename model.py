import json
from nltk.classify import NaiveBayesClassifier
from preprocessing import preprocess_text

def extract_features(text):
    words = preprocess_text(text)
    return {word: True for word in words}

def train_model():
    with open("data/training_data.json", "r") as file:
        training_data = json.load(file)
    training_set = [(extract_features(data['text']), data['intent']) for data in training_data]
    return NaiveBayesClassifier.train(training_set)