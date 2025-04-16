#import all libraries
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json
#load the english spacy things
nlp = spacy.load("en_core_web_sm")

#make title
st.title("NERmy: Named Entity Recognition with Custom Labels!")

# make introduction
st.markdown("""
Welcome! This app lets you explore NER by defining YOUR own custom labels and rules.
You can upload a file or input your own text, then add patterns (e.g., keywords or phrases) and assign labels to them.
""")
# make introduction to NER, just in case they are not super familiar
st.header("But, what is NER?") #header for organization
st.write("""
NER stands for Named Entity Recognition.
             it's a subtask of Natural Language Processing (NLP)
             that focuses on identifying and categorizing important "named entities" within a piece of text.
""") # brief introduction in case the user does not have previous knowledge of NER
#add in more instructions
st.header(" 🔧 how to use the app:")
st.write("""
    1. Go to the sidebar 
    2. Input or upload your text.
    3. Add your custom rules in JSON format: remember to replace the upper case words with what you actually want there!
       ```json
       [
         {"label": "WHAT YOU WANT TO APPEAR WHEN THE WORD APPEARS IN THE TEXT", "pattern": "THE WORD"}
       ] 
    4. Click the button to view results!
""")
# Sidebar for inputs (I chose sidebar because I think it's cute)
st.sidebar.header("✏️Step 1: Input your text") # header to make it organized
input_method = st.sidebar.radio("Choose input method:", ["Manual entry", "Upload .txt file"])#yay multiple optioms
#make if else statements to match what the user's inputed
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
st.sidebar.header("🧩 Step 2: Define Custom Entities") # header for organization
st.sidebar.markdown("Enter patterns as JSON list (e.g., `[{'label': 'Color' , 'pattern': 'orange'}]`)") #markdown text to explain to user
pattern_input = st.sidebar.text_area("Custom patterns:", value="""[
 {"label": "CLASS", "pattern": "Elements of Computing II"},
 {"label": "PROFESSOR", "pattern": "Dr.Smiley"}
]""", height=150) #built in label for student


# code for button/NER output
if st.button("Run NER with Custom Patterns"):
    try:
        custom_patterns = json.loads(pattern_input)#parse the step2 rules into a list of dictionaries to represent custom ent rules

        # Load the spaCy model
        nlp_ruler = spacy.load("en_core_web_sm")

        # Add the EntityRuler by name
        ruler = nlp_ruler.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True}) # replace existing ent predictions with the ones from your custom patterns.

        ruler.add_patterns(custom_patterns) #Inserts the user-defined patterns into the EntityRuler

        # Run NER
        doc = nlp_ruler(text)

        # Display results
        st.subheader("🔎 Detected Entities")
        html = displacy.render(doc, style="ent", page=True)
        st.components.v1.html(html, height=400, scrolling=True)

        # List of entities
        st.subheader("📋 Entity List")
        for ent in doc.ents:
            st.markdown(f"- **{ent.text}** → *{ent.label_}*")

    except Exception as e:
        st.error(f"Sorry! there was an ⚠️ Error: {e} try again later!")