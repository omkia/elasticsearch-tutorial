# An Elasticsearch Tutorial: complete cheatsheet

## Requirements:

1. Anaconda
2. Pycharm
3. Postman
4. Elasticsearch 7.6
5. Postman

## Download and install 
Download and install the .zip elasticsearch package
### Download

Download the .zip archive for Elasticsearch v7.9.0 from: 

https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.0-windows-x86_64.zip

Unzip it with your favourite unzip tool. This will create a folder called elasticsearch-7.9.0, which we will refer to as %ES_HOME%. In a terminal window, cd to the %ES_HOME% directory, for instance:
```
cd c:\elasticsearch-7.9.0
```

### Running Elasticsearch from the command line

Elasticsearch can be started from the command line as follows:

```
.\bin\elasticsearch.bat
```

If you have password-protected the Elasticsearch keystore, you will be prompted to enter the keystore’s password. See Secure settings for more details.

By default, Elasticsearch runs in the foreground, prints its logs to STDOUT, and can be stopped by pressing Ctrl-C.


## Index creation

### LM

in postman set body type=raw then
Put 127.0.0.1:9200/lmd

```
{

  "settings": {
    "index":{
                "similarity" : {
              "default " : {
                "type" : "LMDirichlet",
                "mu" : 2000
              }
            },
      "analysis":{
        "filter":{
          "english_stop":{
            "type":"stop",
            "stopwords":"_english_"
          },
          "my_stemmer":{
            "type":"stemmer",
            "name":"english"
          }
        },
        "analyzer":{
          "my_custom_analyzer":{
            "type":"custom",
            "tokenizer":"standard",
            "filter":[
              "lowercase",
              "english_stop",
              "my_stemmer"
              ]
          }
        }
      }
    },
        "number_of_shards": 1
    },
    "mappings": {
        "properties": {
            "content": {
            "similarity" : "my_similarity" ,
            "analyzer": "my_custom_analyzer",
                "type": "text"
            }
        }
    }
}
```
For more info:
https://www.elastic.co/blog/language-models-in-elasticsearch

### Stop Stemmed index
Put 127.0.0.1:9200/stopstem2
```
{

  "settings": {
    "index":{
      "analysis":{
        "filter":{
          "english_stop":{
            "type":"stop",
            "stopwords":"_english_"
          },
          "my_stemmer":{
            "type":"stemmer",
            "name":"english"
          }
        },
        "analyzer":{
          "my_custom_analyzer":{
            "type":"custom",
            "tokenizer":"standard",
            "filter":[
              "lowercase",
              "english_stop",
              "my_stemmer"
              ]
          }
        }
      }
    },
        "number_of_shards": 1
    },
    "mappings": {
        "properties": {
            "content": {
                "analyzer": "my_custom_analyzer",
                "type": "text"
            }
        }
    }
}
```
## Change index similarity
### changing similarity
post  127.0.0.1:9200/lmd/_close

put  127.0.0.1:9200/lmd/_settings 
Notice that the name of similarity must be default to apply in query
```
{

  "settings": {
    "index":{
                "similarity" : {
              "default" : {
                "type" : "LMDirichlet",
                "mu" : 2000
              }
            }
}}}
```
Post 127.0.0.1:9200/lmd/_open

Post 127.0.0.1:9200/lmd/refresh

### changing analyzer and reindex
Post 127.0.0.1:9200/_reindex
```
{
  "source": {
    "index": "lm2"
  },
  "dest": {
    "index": "lmd"
  }
}
```
## search
GET localhost:9200/lmd/_search
```
{
        "query": {
            "query_string": {
                    "query":"foxes night hell",
                    "analyzer": "my_custom_analyzer",
                    "default_field":"doc.content"
            }
        }
    }
```
## check index
### get index mapping and settings
The analyzer are part of the index settings, you can retrieve them using the get index settings api:
```
curl -XGET 'http://localhost:9200/wazzup/_settings'
```
### check analyzer
The analyze API is an invaluable tool for viewing the terms produced by an analyzer. A built-in analyzer can be specified inline in the request:

POST _analyze
```
{
  "analyzer": "whitespace",
  "text":     "The quick brown fox."
}
```

The API returns the following response:
```
{
  "tokens": [
    {
      "token": "The",
      "start_offset": 0,
      "end_offset": 3,
      "type": "word",
      "position": 0
    },
    {
      "token": "quick",
      "start_offset": 4,
      "end_offset": 9,
      "type": "word",
      "position": 1
    },
    {
      "token": "brown",
      "start_offset": 10,
      "end_offset": 15,
      "type": "word",
      "position": 2
    },
    {
      "token": "fox.",
      "start_offset": 16,
      "end_offset": 20,
      "type": "word",
      "position": 3
    }
  ]
}
```
You can also test combinations of:
•	A tokenizer 
•	Zero or more token filters 
•	Zero or more character filters 

POST _analyze
```
{
  "tokenizer": "standard",
  "filter":  [ "lowercase", "asciifolding" ],
  "text":      "Is this déja vu?"
}
```

The API returns the following response:
```
{
  "tokens": [
    {
      "token": "is",
      "start_offset": 0,
      "end_offset": 2,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "this",
      "start_offset": 3,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "deja",
      "start_offset": 8,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "vu",
      "start_offset": 13,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 3
    }
  ]
}
```


## Delete an index

Delete 127.0.0.1:9200/stopstem2

## opimizations
### increase heap size
In ElasticSearch >= 5 the documentation has changed, which means none of the above answers worked for me.
I tried changing ES_HEAP_SIZE in /etc/default/elasticsearch and in etc/init.d/elasticsearch, but when I ran ps aux | grep elasticsearch the output still showed:
/usr/bin/java -Xms2g -Xmx2g # aka 2G min and max ram 
I had to make these changes in:
```
/etc/elasticsearch/jvm.options
//Xms represents the initial size of total heap space
//Xmx represents the maximum size of total heap space

-Xms1g 
-Xmx1g 
//the settings shipped with ES 5 were: -Xms2g
//the settings shipped with ES 5 were: -Xmx2g
```
### refresh interval
#### While indexing
Put localhost:9200/stopstem2/_settings
```
{
    "index" : {
        "refresh_interval" : 0
    }
}
```
#### after indexing
Put localhost:9200/stopstem2/_settings
```
{
    "index" : {
        "refresh_interval" : 1
    }
}
```
### number of replicas
Put localhost:9200/collectiontsv2pure/_settings
```
{
  "index": {
  "number_of_replicas" : 0
}
}
```

## debugging
### read only index
Put localhost:9200/collectiontsv2pure/_settings
```
{
  "index":{
    "blocks": {
      "write": "false",
      "read_only": "false"
   }
}
}
```
Put localhost:9200/_all/_settings
```
{
    "index.blocks.read_only_allow_delete": false
}
```
### low disk watermark
Put localhost:9200/_cluster/settings
```
{
  "transient": {
    "cluster.routing.allocation.disk.watermark.low": "95%",
    "cluster.routing.allocation.disk.watermark.high": "1gb",
    "cluster.info.update.interval": "1m"
}
}
```
or
```
{
  "transient": {
    "cluster.routing.allocation.disk.watermark.low": "2gb",
    "cluster.routing.allocation.disk.watermark.high": "1gb",
    "cluster.routing.allocation.disk.watermark.flood_stage": "1gb",
    "cluster.info.update.interval": "1m"
}}
```
