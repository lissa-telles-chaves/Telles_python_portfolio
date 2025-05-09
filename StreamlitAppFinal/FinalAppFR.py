#import libraries
import streamlit as st  
from transformers import pipeline 
import gensim #for topic modeling with LDA
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk #for NLP 
import re

# Cache NLTK stopwords and stemmer setup
@st.cache_resource
def load_nltk_resources(): #create a function 
    nltk.download('stopwords') #downloads stopwords dataset so we don't stopwards like "the", "and", etc...
    return set(stopwords.words('english')), SnowballStemmer("english") #returns english stopwords as a set and a stemmer so we reduce all words to their roots

stop_words, stemmer = load_nltk_resources() #call function we just created and unpack returned tuples into two variables.

# Cache the sentiment pipeline
@st.cache_resource
def load_sentiment_pipeline(): #create a function that loads sentiment analysis pipeline from the Hugging Face Transformers library
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_pipeline = load_sentiment_pipeline() #calls function we just created

# Text preprocessing function
def preprocess_text(text):
    text = re.sub(r"[^a-z\s]", "", text.lower()) #convert text to lowercase and remove everything except lowercase letters ans spaces
    return [stemmer.stem(word) for word in text.split() if word not in stop_words] #split text into words, filtering out stopwords, stemming remaining words and make a list witht them

# Topic modeling function
def get_topics(text, num_topics=3): 
    tokens = preprocess_text(text) #preprocess input
    if not tokens: #message for error
        return ["Not enough content for topic modeling."]
    dictionary = corpora.Dictionary([tokens]) #create a Gensim dictionary 
    corpus = [dictionary.doc2bow(tokens)] # and corpus for tokens
    lda_model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42, passes=10) #LDA is a topic model 
    return [topic[1] for topic in lda_model.print_topics()] #return a list of the main topics we found 

# Combined analysis function
def analyze_text(text):
    sentiment = sentiment_pipeline(text)[0] #analyze sentiment of input
    topics = get_topics(text) # extract topics
    return sentiment, topics

# APP UI
st.title("💭QuickFeels: know what someone is saying and the sentiment behind it quickly")
st.markdown("Enter two texts below to compare **sentiment** and explore **topics**.")

text1 = st.text_area("✍️ Text 1", height=150)
text2 = st.text_area("✍️ Text 2", height=150)

if st.button("🔍 Analyze"):
    if not text1.strip() or not text2.strip():
        st.warning("Please enter both texts.")
    else:
        result1, topics1 = analyze_text(text1)
        result2, topics2 = analyze_text(text2)

        col1, col2 = st.columns(2)
        for i, (col, result, topics, label) in enumerate([(col1, result1, topics1, "Text 1"), (col2, result2, topics2, "Text 2")]):
            with col:
                st.subheader(f"{label} Sentiment")
                st.metric("Label", result["label"])
                st.metric("Confidence", f"{result['score']:.2%}")
                st.markdown(f"🧵 {label} Topics")
                for topic in topics:
                    st.markdown(f"- {topic}")
