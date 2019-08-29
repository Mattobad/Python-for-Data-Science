from nltk import pos_tag, word_tokenize
text = word_tokenize("And now for something completely different")
print(text)
pos_tag(text)


from nltk.stem import PorterStemmer
porter = PorterStemmer()
print(porter.stem("planning"))


from nltk.corpus import wordnet as wn
print(wn.synsets('dog'))
print(wn.synsets('dog.n.01').definition())
wn.synsets('happy')

wrd=wn.synset('dog.n.01')
wrd.hypernyms()
