from elasticsearch import Elasticsearch
import json, requests
import csv
import operator
from playsound import playsound


elastic_client =  Elasticsearch(timeout=40, max_retries=10, retry_on_timeout=True)
elastic_client.cluster.health(wait_for_status='yellow', request_timeout=40)
#search Documents by id in elasticsearch
def searchByID(id):
    #sample input
    #id=[ 1234, 'MARCO_1' ]

    # create a Python dictionary for the search query:
    search_param = {
        "query": {
            "terms": {
                "_id": id # find Ids '1234' and '42'
            }
        }
    }

    # get a response from the cluster
    response = elastic_client.search(index="treccast", body=search_param, request_timeout=40)

    all_hits = response['hits']['hits']
    ranking = ""
    rank = 0
    for num, doc in enumerate(all_hits):
        #print(type(doc['_source']['doc']['content']))
        return doc['_source']['doc']['content']


