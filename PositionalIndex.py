import json
import os.path
from os import path

# this function make the Positional Index for all the docs
def Make_PositionalIndex(docs):
    PositionalIndex = {}
    for i in range(len(docs)):
        k=0
        for word in docs[i]:
            if word not in PositionalIndex.keys():
                PositionalIndex[word] = {}
            
            if (i+1) not in PositionalIndex[word]:
                PositionalIndex[word][i+1] = []
            
            PositionalIndex[word][i+1].append(k)
            k+=1

    PositionalIndex= dict(sorted(PositionalIndex.items(), key=lambda item: item[0])) 
    
    return PositionalIndex

# this function reads the already Positional Index stored in a file
def Read_PositionalIndex():
    if path.exists('PositionalIndex.json'):
        PositionalIndex = json.load(open('PositionalIndex.json'))
        return PositionalIndex