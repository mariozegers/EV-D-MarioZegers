import json
import operator

def top10Retweeted():
    listedFile = []
    top10 = []
    for n in range(10):
        top10.append({"retweetCount":0})

    for line in open("farmers-protest-tweets-2021-03-5.json" , 'r'):
        fileLine = json.loads(line)
        listedFile.append(fileLine)
        top10.sort(key=operator.itemgetter('retweetCount'), reverse = True)
        if fileLine["retweetCount"] > top10[9]["retweetCount"]:
            top10[9] = fileLine

    for p in top10:
        print(p["user"]["username"] + ": " +  p["content"])
    return top10
 