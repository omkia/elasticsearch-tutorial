#python code for creating text file oytput for trec eval input
def createRes(dictionary,turn_num,turnname):
    rank=0
    rankings=""

    for word in sorted(dictionary, key=dictionary.get, reverse=True):
        rank=rank+1
        rankings = rankings+(str(turn_num) + " 0 " + str(word) + " " + str(rank) + " " + str(dictionary[word])+ " " + turnname + "\n")
    return rankings