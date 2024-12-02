import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.data.path.append('./nltk_data')


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in words if word.isalnum() and word not in stop_words]