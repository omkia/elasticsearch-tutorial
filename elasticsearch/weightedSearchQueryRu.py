#rerank results that returned by elASTICSEARCH
def weightedSearchQueryRules(query,turn_num,turnname,index):
    #sample input
    #query = 'hi'
    #turn_num= "1_1"


    search_param={
        "query": {
            "query_string": {
                    "query":query,
                    "analyzer": "my_stop_analyzer",
                    "default_field":"doc.content"
            }
        }
    }
    # get another response from the cluster
    response = elastic_client.search(index=index, body=search_param,request_timeout=40, size= "1000")

    all_hits = response['hits']['hits']
    ranking = ""
    rank = 0
    whyList=""
    scores=[]
    # trec eval only see scores of items(so if you change orders of lines the map and other results dont change and moving items with their corresponding scores ,up and down has no effect)
    for num, doc in enumerate(all_hits):
        scores.append(str(doc['_score']))

    for num, doc in enumerate(all_hits):
        if("Why" in query):
            if("because" in doc['_source']['doc']['content']):
                rank = rank + 1
                ranking = ranking + (str(turn_num) + " 0 " + doc["_id"] + " " + str(rank) + " " + scores[rank-1]+ " " + turnname + "\n")
    for num, doc in enumerate(all_hits):
        if("Why" in query):
            if(not("because" in doc['_source']['doc']['content'])):
                rank = rank + 1
        #print ("DOC ID:", doc["_id"], "--->", doc['_source']['doc']['content'],"score: ", doc['_score'], "\n")
                ranking = ranking + (str(turn_num) + " 0 " + doc["_id"] + " " + str(rank) + " " + scores[rank-1] + " " + turnname+"\n")
        else:
            rank = rank + 1
            ranking = ranking + (str(turn_num) + " 0 " + doc["_id"] + " " + str(rank) + " " + scores[rank-1]+ " " + turnname+"\n")
    return ranking