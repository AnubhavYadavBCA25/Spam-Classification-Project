import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import joblib

# Set page title and icon
st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
)
st.sidebar.header("Prediction")

# Function to preprocess text data
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove punctuation
    tokens = [word for word in tokens if word.isalnum()]
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    # Combine the words back into a full text
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

def main():
    # import the trained model and vectorizer
    model = joblib.load(open("notebooks/artifact/model.pkl", "rb"))
    vectorizer = joblib.load(open("notebooks/artifact/tfidf.pkl", "rb"))

    # Header
    st.header("🔮 SMS Spam Classifer", divider='rainbow')
    st.write("Welcome to the SMS Spam Classifier! Enter a message below to determine if it is spam or ham.")
    st.write("Example of Spam Message: 'Congratulations! You've won a free vacation. Text 'WIN' to 12345 to claim your prize.'")
    st.write("Example of Ham Message: 'Hey, what time are we meeting tomorrow?'")
    st.divider()

    # Get user input
    message = st.text_area("Enter a message:")
    if st.button("Classify"):
        # Preprocess the message
        message = preprocess_text(message)
        # Vectorize the message
        message_vector = vectorizer.transform([message])
        # Make prediction
        prediction = model.predict(message_vector)[0]
        # Display prediction
        if prediction == 1:
            st.error("This message is classified as Spam. 🚫")
        else:
            st.success("This message is classified as Ham. ✅")
    st.divider()

    # Note
    st.subheader("⚠️Please Note:")
    st.write("1. The model was trained on the SMS Spam Collection dataset, which contains 5,574 English SMS messages labeled as spam or ham.")
    st.write("2. Number of Spam Messages: 747 (13.4%) | Number of Ham Messages: 4,827 (86.6%).")
    st.write("3. Because of the limitations of the dataset, the model may not be accurate for all messages.")
    st.write("4. Model is not trained on all possible spam messages. It may not classify all spam messages correctly. It is recommended to use caution when classifying messages.")
    st.write("5. This model is able to classify ham messages with high accuracy, but may not be as accurate for spam messages.")
    st.write("6. This model is for educational purposes only and should not be used as a definitive spam detection system.")
    st.write("7. Please use the model as a reference and exercise caution when classifying messages.")
    
    # Footer
    st.markdown("---")
    st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <div style="text-align:center;">
        <p>Made with ❤️ by Anubhav Yadav</p>
        <p>Follow me on 
            <a href="https://linkedin.com/in/anubhav-yadav-srm" target="_blank"><i class="fab fa-linkedin"></i>LinkedIn</a> | 
            <a href="https://github.com/AnubhavYadavBCA25" target="_blank"><i class="fab fa-github"></i>GitHub</a>
        </p>
    </div>
    """, unsafe_allow_html=True
)

if __name__ == "__main__":
    main()