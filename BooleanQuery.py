from nltk.stem import PorterStemmer

def or_query(q1,q2):
    return list(set(q1).union(q2))

def and_query(q1,q2):
     return list(set(q1).intersection(q2))

def SingleKeyword(q,InvertedIndex):
    if q[0]=='not':
        temp = []
        for i in range(1,51):
            temp.append(i)

        if q[1] in InvertedIndex:
            return (list(list(set(temp)-set(InvertedIndex[q[1]])) + list(set(InvertedIndex[q[1]])-set(temp))))
        else:
            return temp

    else:
        if q[0] in InvertedIndex:
            return InvertedIndex[q[0]]
        else:
            return []

def DoubleKeyword(q,InvertedIndex):
    if q[0]=='not' and q[3]=='not':
            res1 = SingleKeyword(q[0:2],InvertedIndex)
            res2 = SingleKeyword(q[3:5],InvertedIndex)
            if q[2]=='and':
                return and_query(res1,res2)
            elif q[2]=='or':
                return or_query(res1,res2)

    elif q[0]=='not':
        res1 = SingleKeyword(q[0:2],InvertedIndex)
        res2 = SingleKeyword(q[3:4],InvertedIndex)
        if q[2]=='and':
            return and_query(res1,res2)
        elif q[2]=='or':
            return or_query(res1,res2)

    elif q[2]=='not':
        res1 = SingleKeyword(q[0:1],InvertedIndex)
        res2 = SingleKeyword(q[2:4],InvertedIndex)
        if q[1]=='and':
            return and_query(res1,res2)
        elif q[1]=='or':
            return or_query(res1,res2)

    elif 'not' in q:
        return "Invalid Syntax of Query!"

    else:
        res1 = SingleKeyword(q[0:1],InvertedIndex)
        res2 = SingleKeyword(q[2:3],InvertedIndex)
        if q[1]=='and':
            return and_query(res1,res2)
        elif q[1]=='or':
            return or_query(res1,res2)

def TripleKeyword(q,InvertedIndex):
    if q[0]=='not' and q[3]=='not' and q[6]=='not':
        res1 = DoubleKeyword(q[0:5],InvertedIndex)
        res2 = SingleKeyword(q[6:8],InvertedIndex)
        if q[5]=='and':
            return and_query(res1,res2)
        elif q[5]=='or':
            return or_query(res1,res2)

    elif q[0]=='not' and q[3]=='not':
        res1 = DoubleKeyword(q[0:5],InvertedIndex)
        res2 = SingleKeyword(q[6:7],InvertedIndex)
        if q[5]=='and':
            return and_query(res1,res2)
        elif q[5]=='or':
            return or_query(res1,res2)
    
    elif q[2]=='not' and q[5]=='not':
        res1 = DoubleKeyword(q[0:4],InvertedIndex)
        res2 = SingleKeyword(q[5:7],InvertedIndex)
        if q[4]=='and':
            return and_query(res1,res2)
        elif q[4]=='or':
            return or_query(res1,res2)
    
    elif q[0]=='not' and q[5]=='not':
        res1 = DoubleKeyword(q[0:4],InvertedIndex)
        res2 = SingleKeyword(q[5:7],InvertedIndex)
        if q[4]=='and':
            return and_query(res1,res2)
        elif q[4]=='or':
            return or_query(res1,res2)
    
    elif q[0]=='not':
        res1 = DoubleKeyword(q[0:4],InvertedIndex)
        res2 = SingleKeyword(q[5:6],InvertedIndex)
        if q[4]=='and':
            return and_query(res1,res2)
        elif q[4]=='or':
            return or_query(res1,res2)
    
    elif q[2]=='not':
        res1 = DoubleKeyword(q[0:4],InvertedIndex)
        res2 = SingleKeyword(q[5:6],InvertedIndex)
        if q[4]=='and':
            return and_query(res1,res2)
        elif q[4]=='or':
            return or_query(res1,res2)
    
    elif q[4]=='not':
        res1 = DoubleKeyword(q[0:3],InvertedIndex)
        res2 = SingleKeyword(q[4:6],InvertedIndex)
        if q[3]=='and':
            return and_query(res1,res2)
        elif q[3]=='or':
            return or_query(res1,res2)
    
    elif 'not' in q:
        return "Invalid Syntax of Query!"
    
    else:
        res1 = DoubleKeyword(q[0:3],InvertedIndex)
        res2 = SingleKeyword(q[4:5],InvertedIndex)
        if q[3]=='and':
            return and_query(res1,res2)
        elif q[3]=='or':
            return or_query(res1,res2)

def MultiKeyword(q,InvertedIndex):
    count = 0
    count += q.count("and")
    count += q.count("or")
    if count == 1:
        return DoubleKeyword(q,InvertedIndex)
    elif count==2:
        return TripleKeyword(q,InvertedIndex)
    else:
        return "Invalid Syntax of Query!"

def B_Query(q,InvertedIndex):
    ps = PorterStemmer() 
    q = q.lower()
    q = q.split()
    q = [ps.stem(word) for word in q]

    if len(q)<=2:
        if len(q)==2 and q[1]=='not':
            return "Invalid Syntax of Query!"
        else:
            return SingleKeyword(q,InvertedIndex)
    else:
        return MultiKeyword(q,InvertedIndex)