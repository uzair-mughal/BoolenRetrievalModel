import json
import os.path
from os import path

# this function make the Positional Index for all the docs
def Make_InvertedIndex(docs):
    InvertedIndex = {}
    for i in range(len(docs)):
        for word in docs[i]:
            if word not in InvertedIndex.keys():
                InvertedIndex[word] = []
            
            if (i+1) not in InvertedIndex[word]:
                InvertedIndex[word].append(i+1)

    InvertedIndex= dict(sorted(InvertedIndex.items(), key=lambda item: item[0])) 
    
    return InvertedIndex

# this function reads the already Positional Index stored in a file
def Read_InvertedIndex():
    if path.exists('InvertedIndex.json'):
        InvertedIndex = json.load(open('InvertedIndex.json'))
        return InvertedIndex