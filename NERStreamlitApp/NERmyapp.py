import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json
nlp = spacy.load('en_core_web_sm')
st.title("NERmy: Named Entity Recognition with Custom Labels")
st.markdown("""
Welcome! This app lets you explore NER by defining YOUR own custom labels and rules.
You can upload a file or input your own text, then add patterns (e.g., keywords or phrases) and assign labels to them.
""")
st.sidebar.header("But, what is NER?")
st.markdown("""
NER stands for Named Entity Recognition.
             it's a subtask of Natural Language Processing (NLP)
             that focuses on identifying and categorizing important "named entities" within a piece of text.
""")
st.sidebar.header("Step 1: Input text")
st.markdown("""
* Attention: when uploading a file, make sure it is in txt format. This App does not support other formats.
""")
input_method = st.sidebar.radio("Choose input method:", ["Manual entry", "Upload .txt file"])
text = ""
if input_method == "Manual entry":
    text = st.sidebar.text_area("Enter your text here:", height=300)
else:
    uploaded_file = st.sidebar.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")

# Sample text option
if not text:
    if st.sidebar.checkbox("Use sample text"):
        text = "I love Elements of Computing II. It is such an interesting class!"

st.sidebar.header("Step 2: Define Custom Entities")
st.sidebar.markdown("Enter patterns as JSON list (e.g., `[{'label': 'CEO', 'pattern': 'Elon Musk'}]`)")

pattern_input = st.sidebar.text_area("Custom patterns:", value="""[
  {"label": "COMPANY", "pattern": "SpaceX"},
  {"label": "FOUNDER", "pattern": "Steve Jobs"}
]""", height=150)

if st.button("Run NER with Custom Patterns"):
    try:
        custom_patterns = json.loads(pattern_input)
        ruler = EntityRuler(nlp, overwrite_ents=True)
        ruler.add_patterns(custom_patterns)

        nlp_ruler = spacy.load("en_core_web_sm")  # Reload to prevent duplicate rules
        nlp_ruler.add_pipe(ruler, before="ner")

        doc = nlp_ruler(text)

        # Display results
        st.subheader("📜 Detected Entities")
        html = displacy.render(doc, style="ent", page=True)
        st.components.v1.html(html, height=400, scrolling=True)

        # List of entities
        st.subheader("📋 Entity List")
        for ent in doc.ents:
            st.markdown(f"- **{ent.text}** → *{ent.label_}*")

    except json.JSONDecodeError:
        st.error("Invalid JSON pattern format. Please check your input.")

