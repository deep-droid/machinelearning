#pip3 install tflearn
#pip3 install tensorflow
#pip3 install --upgrade tensorflow
#pip3 install opencv-python
#pip3 install tqdm
#curses is not supported on this machine (please install/reinstall curses for an optimal experience)
#pip3 install curses
#pip3 install h5py

from nltk.corpus import wordnet

nltk.download()

syns = wordnet.synsets("program")
#synset
print(syns[0].name())
#just the word
print(syns[0].lemmas()[0].name)
#definition
print(syns[0].definition)
#examples
print(syns[0].examples)

synonyms = []
antonyms = []

for syn in wordnet.sysnets("good"):
	for l in syn.lemmas():
		print("l:", l)
		synonyms.append(l.name())
		if l.anonyms():
			anonyms.append(l.antonyms()[0].name())
			
print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2)

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("vessel.n.01")
print(w1.wup_similarity(w2)

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2)

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2)


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2)

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2)
