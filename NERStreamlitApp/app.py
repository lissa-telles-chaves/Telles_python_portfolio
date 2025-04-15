#import all libraries
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json
nlp = spacy.load("en_core_web_sm")

#make title
st.title("NERmy: Named Entity Recognition with Custom Labels!")

# make introduction
st.markdown("""
Welcome! This app lets you explore NER by defining YOUR own custom labels and rules.
You can upload a file or input your own text, then add patterns (e.g., keywords or phrases) and assign labels to them.
""")
# make introduction to NER, just in case they are not super familiar
st.markdown.header("But, what is NER?")
st.write("""
NER stands for Named Entity Recognition.
             it's a subtask of Natural Language Processing (NLP)
             that focuses on identifying and categorizing important "named entities" within a piece of text.
""")
# Sidebar for inputs 
st.sidebar.header("Step 1: Input your text")
input_method = st.sidebar.radio("Choose input method:", ["Manual entry", "Upload .txt file"])


text = ""
if input_method == "Manual entry":
   text = st.sidebar.text_area("Enter your text here:", height=200)
else:
   uploaded_file = st.sidebar.file_uploader("Upload a text file", type=["txt"])
   if uploaded_file:
       text = uploaded_file.read().decode("utf-8")


# Sample text option
if not text:
   if st.sidebar.checkbox("Use sample text"):
       text = "I love Elements of Computing II. Dr. Smiley is a great professor!"


# Sidebar for custom entity patterns 
st.sidebar.header("Step 2: Define Custom Entities")
st.sidebar.markdown("Enter patterns as JSON list (e.g., `[{'label': 'CEO', 'pattern': 'Elon Musk'}]`)")
pattern_input = st.sidebar.text_area("Custom patterns:", value="""[
 {"label": "CLASS", "pattern": "Elements of Computing II"},
 {"label": "PROFESSOR", "pattern": "Dr.Smiley"}
]""", height=150)


# CODE FOR ACTUAL DESIRED OUPUT
if st.button("Run NER with Custom Patterns"):
    try:
        custom_patterns = json.loads(pattern_input)

        # Load the spaCy model
        nlp_ruler = spacy.load("en_core_web_sm")

        # Add the EntityRuler by name
        ruler = nlp_ruler.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})
        ruler.add_patterns(custom_patterns)

        # Run NER
        doc = nlp_ruler(text)

        # Display results
        st.subheader("📜 Detected Entities")
        html = displacy.render(doc, style="ent", page=True)
        st.components.v1.html(html, height=400, scrolling=True)

        # List of entities
        st.subheader("📋 Entity List")
        for ent in doc.ents:
            st.markdown(f"- **{ent.text}** → *{ent.label_}*")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
