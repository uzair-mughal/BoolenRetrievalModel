from nltk.stem import PorterStemmer

def Solve_Query(q,PositionalIndex):
    k = int(q[2][1:])
    DocIds = []
    if q[0] in PositionalIndex.keys():
        for key,value1 in PositionalIndex[q[0]].items():
            if key in PositionalIndex[q[1]].keys():
                value2 = PositionalIndex[q[1]][key]
                i=j=0
                while True:
                    res = int(value2[j])-int(value1[i])
                    if res>=0 and res<=k:
                        DocIds.append(key)
                        break
                    if value2[j]<value1[i]:
                        j+=1
                    elif res>k:
                        i+=1
                    
                    if i >= len(value1):
                        break
                    if j >= len(value2):
                        break
    return DocIds

def P_Query(q,PositionalIndex):
    ps = PorterStemmer() 
    q = q.lower()
    q = q.split()
    if 'and' in q:
        q.remove('and')
    if 'or' in q:
        q.remove('or')
    q = [ps.stem(word) for word in q]

    if len(q) != 3:
        return "Invalid Syntax of Query!"
    elif q[2][0] != '/' or not q[2][1:].isdecimal():
        return "Invalid Syntax of Query!"
    else:
        return Solve_Query(q,PositionalIndex)