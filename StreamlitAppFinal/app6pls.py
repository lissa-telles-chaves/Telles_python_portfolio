import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk
import re
import matplotlib.pyplot as plt
import torch
import numpy as np

# Download NLTK resources
nltk.download('stopwords')

# Load CardiffNLP sentiment model
@st.cache_resource
def load_cardiff_sentiment_pipeline():
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("text-classification", model=model, tokenizer=tokenizer, return_all_scores=True)

sentiment_pipeline = load_cardiff_sentiment_pipeline()

# Preprocessing for topic modeling
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return tokens

def get_topics(text, num_topics=3):
    tokens = preprocess_text(text)
    if not tokens:
        return ["Not enough content for topic modeling."]
    dictionary = corpora.Dictionary([tokens])
    corpus = [dictionary.doc2bow(tokens)]
    lda_model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42, passes=10)
    topics = lda_model.print_topics()
    return [topic[1] for topic in topics]

def classify_sentiment_distribution(text):
    result = sentiment_pipeline(text[:512])[0]  # truncate to 512 tokens
    label_map = {r['label'].lower(): r['score'] for r in result}
    return {
        "Positive": label_map.get("positive", 0),
        "Neutral": label_map.get("neutral", 0),
        "Negative": label_map.get("negative", 0)
    }

def plot_sentiment_pie(distribution, title):
    labels = list(distribution.keys())
    sizes = list(distribution.values())
    colors = ['#4CAF50', '#FFC107', '#F44336']  # Green, Yellow, Red
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title(title)
    ax.axis('equal')
    st.pyplot(fig)

# ---------------- Streamlit UI ----------------
st.title("🧠 Tone and Topic Comparison with Transformers + LDA")

st.markdown("Enter two texts below to compare **sentiment** and explore **topics**.")

text1 = st.text_area("✍️ Text 1", height=150)
text2 = st.text_area("✍️ Text 2", height=150)

if st.button("🔍 Analyze"):
    if not text1.strip() or not text2.strip():
        st.warning("Please enter both texts.")
    else:
        # Sentiment distributions
        dist1 = classify_sentiment_distribution(text1)
        dist2 = classify_sentiment_distribution(text2)

        # Most likely sentiment + confidence
        max_label1 = max(dist1, key=dist1.get)
        max_label2 = max(dist2, key=dist2.get)

        # Topic modeling
        topics1 = get_topics(text1)
        topics2 = get_topics(text2)

        # Display sentiment + pie charts
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Text 1 Sentiment")
            st.metric("Label", max_label1)
            st.metric("Confidence", f"{dist1[max_label1]:.2%}")
            plot_sentiment_pie(dist1, "Text 1 Sentiment")
        with col2:
            st.subheader("Text 2 Sentiment")
            st.metric("Label", max_label2)
            st.metric("Confidence", f"{dist2[max_label2]:.2%}")
            plot_sentiment_pie(dist2, "Text 2 Sentiment")

        # Display topics
        with col1:
            st.markdown("**🧵 Text 1 Topics**")
            for topic in topics1:
                st.markdown(f"- {topic}")
        with col2:
            st.markdown("**🧵 Text 2 Topics**")
            for topic in topics2:
                st.markdown(f"- {topic}")
