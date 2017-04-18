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
#print(all_words.most_common(25))
#print(all_words["stupid"])

word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
		
	return features
	
print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))

featuressets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuressets[:1900]
testing_set = featuressets[1900:]

#classifier - classification
#posterior = prior occurences x likelihood / evedence

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo accuracy %:", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(15)