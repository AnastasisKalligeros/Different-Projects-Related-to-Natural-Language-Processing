# -*- coding: utf-8 -*-
"""
Created on Fri Jul  15 19:33:18 2022

@author: Kalligeros Anastasis
"""
#arxika kanw import to natural language toolkit
import nltk
#kanw import to PunktSentenceTokenizer poy diairei to.txt arxeio 
#se mia lista apo sentences me xrhsh algorithmou
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize, word_tokenize
from nltk.corpus import state_union

#-----------------   2o Thema   ---------------------#


#anoigw to arxeio .txt kai to diavazw 
file = open("C:/Users/tasso/Desktop/EPEXERGASIAFYSIKHSGLWSSAS/randomText.txt","r")
#an to arxeio einai se read mode 
if file.mode == 'r':
    #diavazw to arxeio
    str = file.read()
    
    
#------------  POS Tag List -------------------#

# =============================================================================
# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word
# IN	preposition/subordinating conjunction
# JJ	adjective	'big'
# JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'
# LS	list marker	1)
# MD	modal	could, will
# NN	noun, singular 'desk'
# NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'
# NNPS	proper noun, plural	'Americans'
# PDT	predeterminer	'all the kids'
# POS	possessive ending	parent\'s
# PRP	personal pronoun	I, he, she
# PRP$	possessive pronoun	my, his, hers
# RB	adverb	very, silently,
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# TO	to	go 'to' the store.
# UH	interjection	errrrrrrrm
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# WDT	wh-determiner	which
# WP	wh-pronoun	who, what
# WP$	possessive wh-pronoun	whose
# WRB	wh-abverb	where, when
# =============================================================================
    
   
    
#arxikopoiw ton PunktSentenceTokenizer
    custom_sent_tokenizer = PunktSentenceTokenizer(str)

    tokenized = custom_sent_tokenizer.tokenize(str)

    def process_content():
        try:
            #for each element in tokenized
            for i in tokenized:
                text_words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(text_words)
            #me to chunk pairnoume fraseis apo mh domhmeno keimeno
                chunkGram = r"""Chunk: {<RB>*<VB>*<NNP>+<NN>?}"""
            
                chunkParser = nltk.RegexpParser(chunkGram)
                chunked = chunkParser.parse(tagged)
            
                #print(chunked)
            
                
                #kanw print tis lekseis apo to .txt mazi me thn suntaktikh tous shmasia
                print(tagged)
                #kanw print to syntaktiko dentro kathe protasis
                chunked.draw()
        
        except Exception as e:
            print(str(e))
     # kleinw to arxeio .txt
    file.close()
    
# kalw thn sunarthsh
process_content()
    