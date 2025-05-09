# Welcome to my Final App:  💭 QuickFeels
### Know what someone is saying — and the **sentiment** behind it — quickly.

---

## 🧠 Project Overview

**QuickFeels** is an app that helps users **analyze and compare** two texts. It performs:
- **Sentiment analysis** using a fine-tuned transformer model from Hugging Face.
- **Topic modeling** via Latent Dirichlet Allocation (LDA) to uncover core discussion themes.

This tool is especially helpful for content creators, marketers, researchers, or anyone needing a quick glance at the emotional tone and main topics of textual content.

## 🌟 App Features
### 🔡 User Inputs
- Text 1: First block of text to analyze
- Text 2: Second block of text to compare
- Analyze Button: Triggers analysis for both inputs

### 🧠 Main Functions
- Sentiment Analysis: Uses a pretrained Hugging Face transformer to classify text as Positive or Negative, including a confidence score.

- Topic Modeling: Uses Gensim’s LDA model to extract 3 major topics from each text, after NLP preprocessing (stopwords, stemming, etc.).

### 📊 Outputs
- Side-by-side columns display for each text:
- Sentiment Label
- Confidence Percentage
- 3 Key Topics
## Instructions: 
### 🎥 Demo Video
[Click here to watch the demo video](https://drive.google.com/file/d/10krfWGO3el900onoaBj3yMSdFQMXi0WX/view?usp=drive_link)
### step by step
1️⃣ Launch the App
- If running locally: Run streamlit run your_script_name.py in your terminal.
- If hosted on Streamlit Cloud: Just click the shared URL to open the web app.
2️⃣ Enter Your Texts
- Scroll down to the "✍️ Text 1" and "✍️ Text 2" input areas.
- Paste or type any English-language text you'd like to analyze
3️⃣ Click “🔍 Analyze”
- Press the Analyze button to process both texts. Make sure both fields contain text; otherwise, a warning will appear.
4️⃣ View the Results
- The app displays results in two side-by-side columns:

## 📦 Dependency List
streamlit==1.35.0
transformers==4.40.0
torch>=2.0.0
gensim==4.3.2
nltk==3.8.1

## 🔗 References & Resources
- Streamlit Docs: https://docs.streamlit.io/
- Hugging Face Transformers: https://huggingface.co/docs/transformers/index
- NLTK Documentation: https://www.nltk.org/
- Gensim LDA Topic Modeling:https://radimrehurek.com/gensim/models/ldamodel.html
- Model used: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english