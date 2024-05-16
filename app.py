import streamlit as st

def main():
    st.title("Spam Classification Project")
    st.header("Introduction")
    
    st.write("""
    Welcome to the Spam Classification Project! This project aims to classify messages as either spam or ham (non-spam) using Natural Language Processing (NLP) techniques and machine learning models.""")
    
    st.header("Objective")
    st.write("The primary objective of this project is to develop a robust spam detection system that can accurately identify unsolicited or harmful messages.")

    st.header("How It Works")
    st.write("""
    1. Data Collection: We collect a dataset of messages labeled as spam or ham.
    2. Data Preprocessing: The collected data undergoes preprocessing steps such as tokenization, removing stop words, and transforming text into numerical features.
    3. Model Training: Various machine learning models are trained on the preprocessed data to learn patterns that distinguish spam from ham.
    4. Prediction: The trained models are used to classify new messages as either spam or ham.""")

    st.header("Technologies Used")
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

    st.header("Explore the App")
    st.write("To get started with classifying your own messages, please navigate to the prediction page.")
    
    st.header("About Me")
    st.write("""
    Author: Anubhav Yadav

    Contact: anubhavyadav77ff@gmail.com

    GitHub: [Your GitHub Profile](https://github.com/AnubhavYadavBCA25)
    """)

if __name__ == "__main__":
    main()

