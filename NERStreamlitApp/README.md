# Welcome to NERmy:our Named Entity Recognition App!
## Project Overview: 
### 🎯 Purpose: 
create an app where users can input a text, and the app will highlight entities in the output according to your customized labels utilizing spaCy approach to Named Entity Recognition!
### ❓ But what is spaCy’s? And what is spaCy's approach to Named Entity Recognition?
    spaCy is a Python library for Natural Language Processing (NLP). 
    spaCy's approach to Named Entity Recognition (NER) is uses statistical and neural network-based that have learned to identify and categorize important things (named entities) in text by looking at word patterns and context, often using advanced techniques like neural networks. You can also teach it to recognize new or specific things you care about.
## Tutorial:
[▶️ Watch the demo on Google Drive]([https://drive.google.com/file/d/FILE_ID/view?usp=sharing](https://drive.google.com/file/d/1yKfpmN7WpO1v7xVUc2tcKHa_bEs-w3EE/view?usp=sharing)
### 💡 How to Use This App
1- Choose your input method from the sidebar:
        - Manually type or paste your text.
        - upload a .txt file.
        - Check "Use sample text" if you want to explore without uploading anything.

2- Define your custom entity patterns:
Use JSON format:

json
Copy
Edit
[
  { "label": "LABEL_NAME", "pattern": "Text to detect" }
]
Example:

json
Copy
Edit
[
  { "label": "FOUNDER", "pattern": "Steve Jobs" },
  { "label": "COMPANY", "pattern": "SpaceX" }
]
3- Click “Run NER with Custom Patterns” to apply your rules to the text.

4- View your results:
        - Entities will be highlighted in the text using different colors.
        - A list of detected entities and their labels will also be displayed below the visualization.

## libraries utilized:
- spaCy
- streamlit
## References: 
- https://spacy.io/usage
- https://spacy.io/usage/linguistic-features#named-entities
- https://spacy.io/api/entityruler
