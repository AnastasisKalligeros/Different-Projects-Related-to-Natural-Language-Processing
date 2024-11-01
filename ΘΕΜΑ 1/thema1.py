# -*- coding: utf-8 -*-
"""
Created on Fri Jul  15 15:46:46 2022

@author: Kalligeros Anastasis
"""
#arxika kanw import to natural language toolkit
import nltk



# import sentence tokenizer kai word tokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

#--------------------  1o Thema  ------------------------------#

#anoigw to arxeio .txt kai to diavazw 
file = open("C:/Users/tasso/Desktop/EPEXERGASIAFYSIKHSGLWSSAS/randomText.txt","r")
#an to arxeio einai se read mode 
if file.mode == 'r':
    #diavazw to arxeio
    str = file.read()
    print("List of sentences: \n")
    #kanw print ta sentences apo to randomtext me th xrhsh toy sentence tokenizer
    print(sent_tokenize(str))
    print("\n")
    #kanw print tis lekseis kai ta punctuations apo to randomtext
    print("List of words and punctuations: \n")
    print(word_tokenize(str))
    
    # kleinw to arxeio .txt
    file.close()
































