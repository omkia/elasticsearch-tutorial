#read queries from csv file python and call search function of elasticsearch
def filereader(turnname,index):
    with open("F:\\corefAbbr.csv", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=",")
        ranks = ""
        for line in tsvreader:
            #it bypass first line that say which seperator used in csv file
            if(line[0]=="sep="):
                continue
            print(line)
            #first column of csv file is query id and second is query
            ranks = ranks + searchQuery(line[1].replace("Tell me about", " "), line[0], turnname, index)
        # Write-Overwrites
        resultFile = open(turnname+".txt", "w")  # write mode
        resultFile.write(ranks)#resultFile
        resultFile.close()