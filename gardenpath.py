#=========Setup Spacy
import spacy

nlp = spacy.load('en_core_web_sm')
#========Define our inputs

garden_paths = [
    "Mary gave the child the dog bit a Band-Aid.",
    "The old man the boat.",
    "Helen is expecting tomorrow to be a bad day.",
    "The cotton clothing is made of grows in Mississippi.",
    "That Jill is never here hurts."
]

#========entity recognition

for i in range(0,5):
    nlp_path = nlp(garden_paths[i])
    print([(j, j.label_, j.label) for j in nlp_path.ents])

#garden_paths[0] doesn't assign an entity to Band-Aid
#garden_paths[1] doesn't actually store any entities, which means that neither 'old' or 'old man' is recognised as 'Person'
#garden_paths[3] can only identify Mississippi as an entity
#Spacy did not assign anything I didn't expect, it's more an issue of it not assigning things that I did expect it to assign.