from nltk.stem import PorterStemmer

# this function reads the stop words from file
def read_stopwords():
    stopwords = []
    f = open("Stopword-List.txt","r")
    temp = f.readlines()
    for i in range(len(temp)):
        temp[i] = temp[i].rstrip('\n')
        temp[i] = temp[i].rstrip(' ')
        if temp[i]!='':
            stopwords.append(temp[i])
    return stopwords

# this function removes the puntuations from a given doc
def clean_doc(doc):
    symbols1 = '!.,‘’:@#$%^&?<>*“”()[}{]-—=;/\"\\\t\n'
    symbols2 = '\t\n;?:!.,.—'
    for symb in symbols1:
        if symb in symbols2:
            doc = doc.replace(symb,' ')
        else: 
            doc = doc.replace(symb,'')
    return doc

# this function reads each file and cleans it, tokenize it, remove stopwords and then stem the tokins
def filereader():
    ps = PorterStemmer() 
    stopwords = read_stopwords()
    docs = []
    for i in range(50):
        f = open("ShortStories\\"+str(i+1)+".txt", "r",encoding='utf-8')
        docs.append(f.read().lower())
        docs[i] = clean_doc(docs[i])
        docs[i] = docs[i].split()
        docs[i] = [ps.stem(word) for word in docs[i] if word not in stopwords]
        f.close()
    return docs