import streamlit as st
from transformers import pipeline
import torch

# Load sentiment analysis pipeline
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_pipeline = load_model()

st.title("🤖 Tone Comparison with Transformers")

st.markdown("Enter two pieces of text to compare their **sentiment tone** using a BERT-based model.")

# Text inputs
text1 = st.text_area("Text 1", height=150)
text2 = st.text_area("Text 2", height=150)

# Compare button
if st.button("Compare Sentiment"):
    if not text1.strip() or not text2.strip():
        st.warning("Please enter both texts.")
    else:
        # Get predictions
        result1 = sentiment_pipeline(text1)[0]
        result2 = sentiment_pipeline(text2)[0]

        # Display results
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Text 1")
            st.metric("Label", result1['label'])
            st.metric("Confidence", f"{result1['score']:.2%}")

        with col2:
            st.subheader("Text 2")
            st.metric("Label", result2['label'])
            st.metric("Confidence", f"{result2['score']:.2%}")

        # Summary
        st.subheader("Summary")
        st.write(f"**Text 1 tone:** {result1['label']} ({result1['score']:.2%} confidence)")
        st.write(f"**Text 2 tone:** {result2['label']} ({result2['score']:.2%} confidence)")


