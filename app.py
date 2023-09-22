import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt") as f:
    text = f.read()

doc = nlp(text)

for token in text[:10]:
    print(token)

for token in doc[:10]:
    print(token)

for token in text.split()[:10]:
    print(token)

for sent in doc.sents:
    print(sent)

sentence_1 = list(doc.sents)[0]
token_2 = sentence_1[2]

token_2.text
token_2.left_edge
token_2.right_edge
token_2.ent_type_
token_2.ent_iob_
token_2.lemma_

sentence_1[12]
sentence_1[12].lemma_

token_2.morph
sentence_1[12].morph

token_2.pos_
token_2.dep_
token_2.lang_

text = "Mike enjoys playing football."
doc_2 = nlp(text)
print(doc_2)

for token in doc_2:
    print(token, "\t\t", token.pos_, "\t\t", token.dep_)

displacy.render(doc_2, style="dep")

for ent in doc.ents:
    print(ent.text, ent.label_)

displacy.render(doc, style="ent")
