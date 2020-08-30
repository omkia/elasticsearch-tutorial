#another bulk indexer
import csv
from elasticsearch import Elasticsearch, helpers

# create a new instance of the Elasticsearch client class
elastic = Elasticsearch(timeout=30, max_retries=10, retry_on_timeout=True)
# ...or uncomment to use this instead:
#elastic = Elasticsearch("localhost")


with open("F:\\corefAbbr.csv", encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    docCounter = 0
    turn = 0
    text = ""
    docs = []
    for line in csvReader:
        doc = {}
        docCounter = docCounter + 1

        if line[0] == "" or docCounter<19120000:
            continue
        else:
            docs.append({"_id": line[0],
                "doc": {  # the body of the document
                "content": line[1]
                }
            })
            if docCounter % 5000 == 0:
                print(docCounter)
                try:
                    # make the bulk call using 'actions' and get a response
                    response = helpers.bulk(elastic, docs, index='treccast')
                    print("\nactions RESPONSE:", response)
                    docs.clear()
                except Exception as e:
                    print("\nERROR:", e)

    try:
        # make the bulk call using 'actions' and get a response
        response = helpers.bulk(elastic, docs, index='treccast')
        print("\nactions RESPONSE:", response)
    except Exception as e:
        print("\nERROR:", e)
