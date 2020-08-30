#elasticsearch bulk indexer python
#index from csv
from elastic import Elastic
import json
from elasticsearch import Elasticsearch
from config import ELASTIC_HOSTS, ELASTIC_SETTINGS
import csv

def main():
    index_name = "collectiontsv2pure"

    mappings = {
        "content": Elastic.analyzed_field(),
    }

    duparray=[]


    # with open('duplicates.txt', 'w') as f:
    #     for item in duparray:
    #         f.write("%s\n" % item)
    alldocs = {}
    elastic = Elastic(index_name)
    # elastic.delete_index()
    es = Elasticsearch(hosts=ELASTIC_HOSTS,timeout=30, max_retries=10, retry_on_timeout=True)
    num=0
    with open("F:\\treccar.csv", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=",")
        i=0
        for line in tsvreader:
            doc = {}
            i = i + 1
            if(line[1]=='' or i<2750000):
                continue

            doc['content'] = line[1]
            alldocs[line[0]] = doc

            if((i%50000)==0):
                elastic.add_docs_bulk(alldocs)
                # print(alldocs)
                alldocs.clear()
                print(i)

    if (es.indices.exists(index_name)):
        elastic.add_docs_bulk(alldocs)
        print(" index updated")

    else:
        elastic.create_index(mappings)
        elastic.add_docs_bulk(alldocs)
        print("new index created")


if __name__ == "__main__":
    main()