# find relevant answers in qrel file
def findRelAns(turnnum):

  #c=(urllib.request.urlopen('https://raw.githubusercontent.com/daltonj/treccastweb/master/2019/data/training/train_topics_mod.qrel').read()).decode('ascii')
  #lines = c.split("\n")
  veryRel=[]
  Rel=[]
  with open("train_topics_mod.qrel") as file_in:
      for line in file_in:
        print("line  "+line)
        x = str(line).split(" ")
        print(x)
        if(x[0]==turnnum and x[3]=="1\n"):
          Rel.append(x[2])
        if(x[0]==turnnum and x[3]=="2\n"):
          veryRel.append(x[2])
      veryRel.extend(Rel)
      return veryRel