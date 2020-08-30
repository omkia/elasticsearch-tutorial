def weightedSearchQuery(part1,part2,part3,turn_num,turnname,index):
    #sample input
    #query = 'hi'
    #turn_num= "1_1"

    query = "(" + part1 + ")^1 (" + part2 + ")^2 (" + part3 + ")^3"

    search_param={
        "query": {
            "query_string": {
                    "query":query,
                    "analyzer": "my_custom_analyzer",
                    "default_field":"doc.content"
            }
        }
    }
    # get another response from the cluster
    response = elastic_client.search(index=index, body=search_param,request_timeout=40, size= "1000")


    all_hits = response['hits']['hits']
    ranking = ""
    rank = 0



    for num, doc in enumerate(all_hits):
        ranking = ranking + (str(turn_num) + " 0 " + doc["_id"] + " " + str(rank) + " " + str(
            doc['_score']) + " " + turnname+"\n")

    return ranking