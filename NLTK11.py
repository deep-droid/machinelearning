#pip3 install tflearn
#pip3 install tensorflow
#pip3 install --upgrade tensorflow
#pip3 install opencv-python
#pip3 install tqdm
#curses is not supported on this machine (please install/reinstall curses for an optimal experience)
#pip3 install curses
#pip3 install h5py

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]
			
# documents = []
# for category in movie_reviews.categories():
	# for fileid in movie_reviews.fileid(category):
		# documents.append(list(movie_reviews.words(fileid), category)

random.shuffle(documents)
		
#print(documents[1])

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)	
print(all_words.most_common(25))

print(all_words["stupid"])
	