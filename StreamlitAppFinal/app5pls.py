import streamlit as st # to build app
from transformers import pipeline #for the sentiment analysis mainly
import gensim #
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk
import re

# Download NLTK resources
nltk.download('stopwords')

# Load sentiment pipeline once
@st.cache_resource
def load_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_pipeline = load_sentiment_pipeline()

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

# ---------------- Streamlit UI ----------------
st.title("💭QuickFeels: know what someone is saying and the sentiment behind it quickly")

st.markdown("Enter two texts below to compare **sentiment** and explore **topics**.")

text1 = st.text_area("✍️ Text 1", height=150)
text2 = st.text_area("✍️ Text 2", height=150)

if st.button("🔍 Analyze"):
    if not text1.strip() or not text2.strip():
        st.warning("Please enter both texts.")
    else:
        # Run sentiment analysis
        result1 = sentiment_pipeline(text1)[0]
        result2 = sentiment_pipeline(text2)[0]

        # Run topic modeling
        topics1 = get_topics(text1)
        topics2 = get_topics(text2)

        # Display sentiment
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Text 1 Sentiment")
            st.metric("Label", result1["label"])
            st.metric("Confidence", f"{result1['score']:.2%}")
        with col2:
            st.subheader("Text 2 Sentiment")
            st.metric("Label", result2["label"])
            st.metric("Confidence", f"{result2['score']:.2%}")
        with col1:
            st.markdown("🧵 Text 1 Topics")
            for topic in topics1:
                st.markdown(f"- {topic}")
        with col2:
            st.markdown("🧵 Text 2 Topics")
            for topic in topics2:
                st.markdown(f"- {topic}")
