import spacy

nlp = spacy.load("en_core_web_sm")
text = "Apple is looking at buying a startup in London for $1 billion."

doc = nlp(text) # feldolgozza a szöveget
for ent in doc.ents:
	print(ent.text, "->", ent.label_) # kiírja a felismert entitásokat és típusokat