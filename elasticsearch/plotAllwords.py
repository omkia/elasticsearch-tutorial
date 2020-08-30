#Checking if string 'Mary' exists in dictionary value
relevantList= (search(allLinesDict, 'Mary')) #prints firstName
alltokens=[]
for key in relevantList:
  for id in findRelAns(key):
    doc=searchByID([id])
    if(doc!=None):
        stopRemovedDoc = StopRemoval(doc).replace("."," ").replace(")"," ").replace("("," ").replace(":"," ")
        TokenizedArray = word_tokenize(stopRemovedDoc)
        alltokens.extend(TokenizedArray)

plotFreq(alltokens,30)