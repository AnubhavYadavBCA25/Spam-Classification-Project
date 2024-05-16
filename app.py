import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.sidebar.success("Select a demo above.")

def main():
    st.title("✉️ Spam Classification Project")
    st.divider()
    
    st.header("Introduction 📚")
    st.write("""
    Welcome to the Spam Classification Project! This project aims to classify messages as either spam or ham (non-spam) using Natural Language Processing (NLP) techniques and machine learning models.""")
    st.divider()

    st.header("What is Spam? 🤔")
    st.write("Spam is unsolicited or unwanted messages sent in bulk, typically for commercial purposes. These messages are often irrelevant, misleading, or harmful to the recipient.")
    st.divider()

    st.header("Objective 🎯")
    st.write("The primary objective of this project is to develop a robust spam detection system that can accurately identify unsolicited or harmful messages.")
    st.divider()

    st.header("How It Works 🛠️")
    st.write("""
    1. Data Collection: We collect a dataset of messages labeled as spam or ham.
    2. Data Preprocessing: The collected data undergoes preprocessing steps such as tokenization, removing stop words, and transforming text into numerical features.
    3. Model Training: Various machine learning models are trained on the preprocessed data to learn patterns that distinguish spam from ham.
    4. Prediction: The trained models are used to classify new messages as either spam or ham.""")
    st.divider()

    st.header("Technologies Used 💻")
    st.write("""
    - Python: For coding the project.
    - Pandas: For data manipulation and analysis.
    - Matplotlib and Seaborn: For data visualization.
    - NLTK and SpaCy: For natural language processing.
    - WordCloud: For generating word clouds.
    - TF-IDF: For text vectorization.         
    - Streamlit: For building the interactive web application.
    - scikit-learn: For machine learning model training and evaluation.
    - MySQL: For storing user inputs and their classifications.""")
    st.divider()

    st.header("Explore the App 🚀")
    st.write("To get started with classifying your own messages, please navigate to the prediction page.")
    st.divider()

    st.header("About Me 🙋‍♂️")
    st.write("""
    Author: Anubhav Yadav

    Contact: anubhavyadav77ff@gmail.com

    GitHub: AnubhavYadavBCA25(https://github.com/AnubhavYadavBCA25)
             
    LinkedIn: Anubhav Yadav(https://www.linkedin.com/in/anubhav-yadav-srm/)
    """)

if __name__ == "__main__":
    main()

