def searchQuery(query,turn_num,turnname,index):
    #sample input
    #query = 'hi'
    #turn_num= "1_1"

    # Python dictionary object representing an Elasticsearch JSON query:
    search_param = {
        "size": 1000,
        'query': {
            'match': {
                'doc.content': query,
            }
        }
    }



#stemmer
#for stop word removed and stemmed index
    search_param2 ={
        "query": {
            "match": {
                "doc.content": {
                    "query": query,
                    "analyzer": "my_custom_analyzer"
                }
            }
        }
    }


    # get another response from the cluster
    response = elastic_client.search(index=index, body=search_param2,request_timeout=40, size= "1000")
    all_hits = response['hits']['hits']
    ranking = ""
    rank = 0
    for num, doc in enumerate(all_hits):
        rank=rank+1
        print ("DOC ID:", doc["_id"], "--->", doc['_source']['doc']['content'],"score: ", doc['_score'], "\n")
        ranking = ranking + (str(turn_num) + " 0 " + doc["_id"] + " " + str(rank) + " " + str(
            doc['_score']) + " " + turnname+"\n")


    return ranking