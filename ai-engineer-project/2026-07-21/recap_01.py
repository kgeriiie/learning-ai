import spacy

nlp = spacy.load("en_core_web_sm")
text = "Thank you for downloading PyCharm! Your download should start shortly. If it doesn't, please use the direct link. How to Google it?"

doc = nlp(text)

print(doc.text)

for ent in doc:
    stwrd = "False"
    if ent.is_stop:
        stwrd = "True"

    print(ent.text + ", lemma: " + ent.lemma_ + ", isStopWorld: " + stwrd)