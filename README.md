# Advance-AI-Project
to install all requirements run in cmd:
pip install -r requirements.txt

./datasets 
- Contains json files with objects relate to news
    - Three important components are : category, headline, short description
AAI_Event_Extraction.ipynb:
    - This is the first model of the paper. The paper is in notebook and result is showned automatically
Improved KNWGRAPH:
    - Implementation of the Knowledge Graph model.

distantSearch.py 
- Provide example of distant supervision, the dataset of this program is in datasets/distant/
- to compile :
    - python distantSearch.py csv_file folder_name
    - python distantSearch.py currency.csv currency

relation_examples.py
- A short example on how to extract relation using first order logic
- compile: python relation_examples.py
- Some additional library needs to be install if there is errors, do this in terminal if needed: pip install library_name 

relation.py
- Example of implemented rules and knowledge inference from first order logic
- The variable can modify to add knowledge
- rules in ./datasets/rules.txt are used for this program
- compile: python relation.py
