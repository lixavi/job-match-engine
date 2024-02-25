import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    # Removing punctuation and stop words
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def calculate_text_similarity(text1, text2):
    tokens1 = preprocess_text(text1)
    tokens2 = preprocess_text(text2)

    # Calculate the Jaccard similarity
    intersection = len(set(tokens1).intersection(tokens2))
    union = len(set(tokens1).union(tokens2))
    jaccard_similarity = intersection / union if union != 0 else 0

    return jaccard_similarity
