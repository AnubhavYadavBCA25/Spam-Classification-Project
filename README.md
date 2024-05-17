# Spam Classification Project

## General Structure of this Project
- Title : SMS Spam Collection Analysis/Prediction
- Description : In this project we have a dataset of SMS's which have a label whether the message is spam or ham (not spam). We are going to analysis the whole dataset, preprocess it using NLTK (NLP Python Library) Module, perform EDA and predict whether the SMS is spam or not.

## Content
### About the Dataset:
- Source of Dataset : https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
- Context : The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam.

- The files contain one message per line. Each line is composed by two columns: v1 contains the label (ham or spam) and v2 contains the raw text.

This corpus has been collected from free or free for research sources at the Internet:

- A collection of 425 SMS spam messages was manually extracted from the Grumbletext Web site. This is a UK forum in which cell phone users make public claims about SMS spam messages, most of them without reporting the very spam message received. The identification of the text of spam messages in the claims is a very hard and time-consuming task, and it involved carefully scanning hundreds of web pages.

- A subset of 3,375 SMS randomly chosen ham messages of the NUS SMS Corpus (NSC), which is a dataset of about 10,000 legitimate messages collected for research at the Department of Computer Science at the National University of Singapore. The messages largely originate from Singaporeans and mostly from students attending the University. These messages were collected from volunteers who were made aware that their contributions were going to be made publicly available.

- A list of 450 SMS ham messages collected from Caroline Tag's PhD Thesis.

- Finally, we have incorporated the SMS Spam Corpus v.0.1 Big. It has 1,002 SMS ham messages and 322 spam messages and it is public available.

## Project Goal:
- The main goal or aim of this project is to analyze the dataset and build a spam classification web application, so user can input their SMS and predict whether the SMS is spam or not.

## Installation (Libraries, IDE and etc):
1. IDE: 
- VSCode : Data Analysis, ML Modelling and Web App. Development (Prefered)
- PyCharm : Data Analysis, ML Modelling and Web App. Development (Prefered)
- Jupyter Notebook : Analysis and ML Modelling, But, not for Web App. Develpoment
- Google Colab : Analysis and ML Modelling, But, not for Web App. Develpoment
2. Python Virtual Enviornment v3.8 (Prefered)
3. Python Libraries:
- Pandas (Data Manipulation)
- NLTK (Text Preprocessing)
- Matplotlib (Data Visualization)
- Scikit-learn (Machine Learning Model)
- Streamlit (Web Application)
- Wordcloud (Text Visualization)
- Plotly (Interactive Visualization)
- Joblib (Model and Vectorizer Pickling/Unpickling)
- MySQL Connection Python (Database Connection) (*Optional)

## Step By Step Project Overview:
1. Setup your 'venv', 'setup.py' file and 'requirements.txt' file.
2. Create a 'notebooks' folder which consist your all analysis and predict model stuff.
3. Perform EDA on your dataset (spam.csv): exploration, text preprocessing, visualization and at last save your cleaned or preprocessed dataset in data folder.
4. Perform model training on your 'cleaned dataset' like: data spliting, vectorization using tf-idf, training and evaluating different models, selecting best performing model based on 'accuracy score', perform model test on unseen or new data and at the last save final best model 'model.pkl' file and vectorizer 'tfidf.pkl' file in artifact folder.
5. Create streamlit web application with different pages (multi-page web application):
- Home Page: Project Introduction, Objective, Tools & Tech. etc.
- Exploration Page: Data Analysis, Visualization and Conclusion.
- Prediction Page: SMS Classifier
6. (Optional) You can store the user input text data from prediction page to your MySQL database for further improvement of model. Although, I just deployed the prediction part, not data storage in database. But, code for performing data storage in database is given in the Prediction.py file.
7. Finally, I prototype project for "Spam Classification" is completed. Please, give your feedback and explore my project from my GitHub.

## Contact
- LinkedIn : https://www.linkedin.com/in/anubhav-yadav-srm/
- Email : anubhavyadav77ff@gmail.com