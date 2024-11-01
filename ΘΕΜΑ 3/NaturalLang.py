
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:43:03 2022

@author: Kalligeros Anastasis
"""

import nltk
import random
from nltk.corpus import genesis
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet, movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier

import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode
import os
from sklearn.ensemble import VotingClassifier



#--------------- Semantic Analysis ---------------------#





#we have two .txt files filled with positive and negative reviews each.
#we gain access to the files   
short_pos = open(file = 'C:/Users/tasso/Desktop/EPEXERGASIAFYSIKHSGLWSSAS/positive.txt',mode = 'r').read()
short_neg = open(file = 'C:/Users/tasso/Desktop/EPEXERGASIAFYSIKHSGLWSSAS/negative.txt', mode = 'r').read()
    

#empty lists 
documents = []
all_words = []

# we take part of speech tags for better results
# J is adject, R is adverb, V is verb
allowed_word_types = ["J", "R", "V"]

#we split the reviews from positive.txt for each new line
for p in short_pos.split('\n'):
    documents.append((p, "pos"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
# for w in part of speech if the word is J, R or V we append it   
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
 
#same procedure for the negative reviews
for p in short_neg.split('\n'):
    documents.append((p, "neg"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
            
            
save_documents = open("pickled_docs.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()
            
    
    
all_words = nltk.FreqDist(all_words)

#we check the top 5000 words to find the features
word_features = list(all_words.keys())[:5000]

save_word_features = open("pickled_features.pickle", "wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        #we get a boolean true if the words are inside the document
        #false if they are not
        features[w] = (w in words)
    return features

#if the words are inside the document with the 5000 most common words
#then it's true
featuresets = [(find_features(rev), category) for (rev, category) in documents]

save_featuresets = open("pickled_featuresets.pickle", "wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()

random.shuffle(featuresets)

#the first 5000 we train and the second 5000 we test
#
training_set = featuresets[:5000]
testing_set = featuresets[5000:]





# =============================================================================
# classifier_f = open("naivebayes.pickle","rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()
# =============================================================================

#negative data
# =============================================================================
# training_set = featuresets[100:]
# testing_set = featuresets[:100]
# =============================================================================

# we train our training set with naive bayes algo
classifier = nltk.NaiveBayesClassifier.train(training_set)
classifier.show_most_informative_features(15)
print("Naive Bayes Algo accuracy percent: ", 
      (nltk.classify.accuracy(classifier, testing_set))*100)

#we imported pickle so we can save our algorithms
#and to help the program run faster
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


#we import some algorithms from sklearn library to test different algos
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent: ", 
      (nltk.classify.accuracy(MNB_classifier, testing_set))*100)


save_classifier = open("MNBAlgo.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent: ", 
      (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)


save_classifier = open("BernoulliNB.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()



LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent: ", 
      (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)


save_classifier = open("LogisticRegression.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()


SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent: ", 
      (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)


save_classifier = open("SGDAlgo.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()


LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent: ", 
      (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)


save_classifier = open("LinearSVCAlgo.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()


NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent: ", 
      (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)


save_classifier = open("NuSVCAlgo.pickle","wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()



# =============================================================================
# voted_classifier = VoteClassifier(
#     NuSVC_classifier,
#     LinearSVC_classifier,
#     MNB_classifier,
#     BernoulliNB_classifier,
#     LogisticRegression_classifier)
# 
# print("voted_classifier accuracy percent: ", 
#       (nltk.classify.accuracy(voted_classifier, testing_set))*100)
# =============================================================================


#---------------- Sentiment Analysis ----------------#

# =============================================================================
# def sentiment(text):
#     feats = find_features(text)
#     
#     return NuSVC_classifier.classify(feats), voted_classifier.confidence(feats)
# 
# =============================================================================

#----------------  Corpora How to tokenize a file from corpora nltk.data  ----------#

# =============================================================================
# sample = genesis.raw("english-web.txt")
# tokenized = sent_tokenize(sample)
# 
# 
# print(tokenized)
# =============================================================================





#------------   WordNet example   -------------------------------#


# =============================================================================
# syns = wordnet.synsets("program")
# 
# print(syns)
# 
# #print synset
# print(syns[0].name())
# 
# #print just the word plan
# print(syns[0].lemmas()[0].name())
# 
# #definition of the word plan and examples
# print(syns[0].definition())
# print(syns[0].examples())
# 
# synonyms = []
# antonyms = []
# 
# for syn in wordnet.synsets("good"):
#     for lemma in syn.lemmas():
#         print(lemma)
#         synonyms.append(lemma.name())
#         if lemma.antonyms():
#             antonyms.append(lemma.antonyms()[0].name())
# 
# print(set(synonyms))
# print(set(antonyms))
# =============================================================================


# ------------------- Semantic similarity -----------------------#


# =============================================================================
# w1 = wordnet.synset("ship.n.01")
# w2 = wordnet.synset("boat.n.01")
# =============================================================================

# compare the two words how similar % in percentage
# =============================================================================
# print(wn.synset(w1.name()).wup_similarity(wn.synset(w2.name())))
# =============================================================================


#--------------------  Text Classification --------------#


# =============================================================================
# doc = []
# doc = [(list(movie_reviews.words(fileid)),category)
#        for category in movie_reviews.categories()
#        for fileid in movie_reviews.fileids(category)]
# 
# random.shuffle(doc)
# 
# print(doc[1])
# 
# #list
# all_words = []
# for w in movie_reviews.words():
#     all_words.append(w.lower())
# 
# 
# all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(10))
# 
# print(all_words["beautiful"])
# 
# word_features = list(all_words.keys())[:3000]
# 
# print(word_features)
# 
# featuresets = [()]
# =============================================================================


# =============================================================================
# class VoteClassifier(ClassifierI):
#     def __init__(self, *classifiers):
#         self._classifiers = classifiers
#         
#     def classify(self, features):
#         votes = []
#         for c in self.classifiers:
#             v = c.classify(features)
#             votes.append(v)
#         return mode(votes)
#     
#     
#     def confidence(self, features):
#         votes = []
#         for c in self._classifiers:
#             v = c.classify(features)
#             votes.append(v)
#             
#         choice_votes = votes.count(mode(votes))
#         conf = choice_votes / len(votes)
#         return conf
# =============================================================================























