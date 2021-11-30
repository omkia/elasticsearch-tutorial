# Python quick start



## creating venv
Virtual Environments (virtualenv or venv) help keep our project dependencies separated to avoid such conflicts 

between package versions and different versions of the Python runtime.

https://realpython.com/python-virtual-environments-a-primer/

## requirements.txt

save package versions for future use
```
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2

// capture requirements to install
pip freeze > requirements.txt

// install requirements from requirements.txt
pip install -r requirements.txt

// or
$ env1/bin/pip freeze > requirements.txt
$ env2/bin/pip install -r requirements.txt
```

## trec eval

standard result for analysing your code performance

https://github.com/joaopalotti/trectools

https://github.com/cvangysel/pytrec_eval

