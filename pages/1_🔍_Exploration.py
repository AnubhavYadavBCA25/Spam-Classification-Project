import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set page title and icon
st.set_page_config(
    page_title="Exploration",
    page_icon="🔍",
)

st.sidebar.header("Data Exploration")

def main():
    st.title("🔍 Data Exploration")
    st.divider()

    st.header("Data Overview 📊", divider='rainbow')
    st.write("Let's start by exploring the dataset contents.")
    
    # Load the dataset
    df = pd.read_csv("notebooks/data/spam.csv", encoding="ISO-8859-1")
    df = df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    df.columns = ["label", "message"]
    df['length'] = df['message'].apply(len)
    # Display the dataset
    st.dataframe(df, width=800, height=400)
    st.divider()
    
    st.header("Data Visualization 📊", divider='rainbow')
    st.write("Let's visualize the dataset to gain more insights.")
    
    # Plot histogram of message lengths
    fig = px.histogram(df, x="length", title="Distribution of Message Lengths")
    st.plotly_chart(fig)
    st.write("Conclusion: The distribution of message lengths varies between spam and ham messages. Spam messages tend to be shorter than ham messages.")
    st.divider()

    # Plot histogram of message lengths by label
    fig = px.histogram(df, x="length", color="label", title="Distribution of Message Lengths by Label", color_discrete_map={'ham':'blue', 'spam':'red'})
    st.plotly_chart(fig)
    st.write("Conclusion: Ham messages tend to be longer than spam messages.")
    st.divider()

    # Plot pie chart of label distribution
    fig = px.pie(df, names="label", title="Label Distribution")
    st.plotly_chart(fig)
    st.write("Conclusion: The dataset contains more ham messages than spam messages.")
    st.divider()
    
    # Generate word cloud of spam messages
    spam_messages = " ".join(df[df["label"] == "spam"]["message"].values)
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(spam_messages)
    
    # Display word cloud
    st.write("Word Cloud of Spam Messages")
    st.image(wordcloud.to_array(), caption="Word Cloud of Spam Messages")
    st.divider()

    # Generate word cloud of ham messages
    ham_messages = " ".join(df[df["label"] == "ham"]["message"].values)
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(ham_messages)

    # Display word cloud
    st.write("Word Cloud of Ham Messages")
    st.image(wordcloud.to_array(), caption="Word Cloud of Ham Messages")
    st.divider()

    st.header("Conclusion 🎯", divider='rainbow')
    st.write("""
    - The dataset contains 5,572 messages labeled as spam or ham.
    - The distribution of message lengths varies between spam and ham messages.
    - The dataset contains more ham messages than spam messages.
    - The word clouds provide a visual representation of the most frequent words in spam and ham messages.
    - Further analysis and modeling can be performed to classify messages as spam or ham.
    """)

if __name__ == "__main__":
    main()