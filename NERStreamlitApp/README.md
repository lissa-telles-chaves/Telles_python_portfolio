# Welcome to NERmy:our Named Entity Recognition App!
## Project Overview: 
### 🎯 Purpose: 
create an app where users can input a text, and the app will highlight entities in the output according to your customized labels utilizing spaCy approach to Named Entity Recognition!
### ❓ But what is spaCy’s? And what is spaCy's approach to Named Entity Recognition?
    spaCy is a Python library for Natural Language Processing (NLP). 
    spaCy's approach to Named Entity Recognition (NER) is uses statistical and neural network-based that have learned to identify and categorize important things (named entities) in text by looking at word patterns and context, often using advanced techniques like neural networks. You can also teach it to recognize new or specific things you care about.
## Tutorial:
▶️ Watch a demo [https://drive.google.com/file/d/FILE_ID/view?usp=sharing](https://drive.google.com/file/d/1yKfpmN7WpO1v7xVUc2tcKHa_bEs-w3EE/view?usp=sharing)
 #### 💡 How to Use This App

1. **Choose your input method** from the sidebar:
   - Manually type or paste your text
   - Or upload a `.txt` file

2. *(Optional)* Check **"Use sample text"** if you want to explore without uploading anything

3. **Define your custom entity patterns**:
   - Use JSON format:  
     ```json
     [
       { "label": "LABEL_NAME", "pattern": "Text to detect" }
     ]
     ```
   - Example:
     ```json
     [
       { "label": "FOUNDER", "pattern": "Steve Jobs" },
       { "label": "COMPANY", "pattern": "SpaceX" }
     ]
     ```

4. **Click “Run NER with Custom Patterns”** to apply your rules to the text

5. **View your results**:
   - Entities will be highlighted in color
   - A list of detected entities and their labels is displayed below

## 🚀 Features
- Input your own text or upload a `.txt` file
- Use sample text to quickly try the app
- Define custom entity labels and patterns in JSON
- Visualize detected entities with colors using spaCy’s `displacy`
- See a list of all entities and their types
## 📚 libraries utilized:
- spaCy
- streamlit
## ✍️ References: 
- https://spacy.io/usage
- https://spacy.io/usage/linguistic-features#named-entities
- https://spacy.io/api/entityruler
