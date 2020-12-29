from preprocessing import *
from modules import *

# Calulate word Frequency of query document 
def wordFreqA(bowA, wordDictA):
	for word in bowA:
	    wordDictA[word]+=1

# Calculate word frequency of source parsed
def wordFreqB(bowB, wordDictB): 
	for word in bowB:
	    wordDictB[word]+=1

# Compute Term Frequency
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        try:
        	tfDict[word] = count/float(bowCount)
        except Exception as err:
        	continue	
    return tfDict

# Compute Inverse Document Frequency
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)+1
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

# Compute Inverse Inverse Document Frequency
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]	   
    return tfidf

# Calculate similarity of query and source documents
def similarity(tfBowA, tfBowB, bowA, bowB):
	sum =0
	totalSum=0
	for commonToken in set(bowA).intersection(set(bowB)):
		sum+= min(tfBowA[commonToken] *len(bowA),tfBowB[commonToken]*len(bowB))
	for val in tfBowA.values():
		totalSum+= val

	if totalSum==0:
		return 0
	else:	
		return (sum)/(totalSum*len(bowA))

# def generateQuery(tfBowA):
# 	tfBowA_sorted = dict( sorted(tfBowA.items(), key=operator.itemgetter(1),reverse=True))
# 	query = ""
# 	for key,value in tfBowA_sorted.items():
# 		if value!=0:
# 			query+=key+" "

# 	return query


