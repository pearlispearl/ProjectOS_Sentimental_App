import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import plotly.graph_objects as go

nltk.download('stopwords')
nltk.download('wordnet')

def visualize_pie_chart(probabilities, classes):
    fig = go.Figure(data=[go.Pie(
        labels=classes,
        values=probabilities,
        marker=dict(colors=['red', 'yellow', 'green']),  # Customize colors
        hole=0.3  # for donut style, optional
    )])
    fig.update_layout(title_text='Sentiment Distribution')
    st.plotly_chart(fig)


stopwords_set = set(stopwords.words('english'))

def preprocess_text(text):
    # Remove HTML tags
    text = re.sub('<[^>]*>', '', text)
    # Remove non-alphanumeric characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Lowercase text
    text = text.lower()
    # Tokenize text
    tokens = text.split()
    # Remove stop words
    tokens = [word for word in tokens if word not in stopwords_set]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Join tokens back into a string
    return ' '.join(tokens)

# Load the saved model, vectorizer, and label encoder
try:
    model, vectorizer, label_encoder = joblib.load('sentiment_model_bow.joblib')
except FileNotFoundError:
    model, vectorizer, label_encoder = joblib.load('sentiment_model_tfidf.joblib')

st.title('Sentiment Analysis App')

user_input = st.text_area('Enter your post here:')

if st.button('Predict'):
    if user_input:
        preprocessed_input = preprocess_text(user_input)
        vectorized_input = vectorizer.transform([preprocessed_input])
        probs = model.predict_proba(vectorized_input)[0]
        classes = label_encoder.classes_
        predicted_index = model.predict(vectorized_input)[0]
        predicted_sentiment = label_encoder.inverse_transform([predicted_index])[0]

        st.write(f'Predicted Sentiment: {predicted_sentiment} with probability {probs[predicted_index]:.4f}')

        # Show pie chart for all class probabilities
        visualize_pie_chart(probabilities=probs, classes=classes)
        
    else:
        st.write('Please enter a post.')