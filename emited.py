import json

def top10Emited():
    listedFile = []
    top10 = []
    for n in range(10):
        top10.append({"user": {"statusesCount":0, "username":""}})

    for line in open("farmers-protest-tweets-2021-03-5.json" , 'r'):
        specialCase = False
        fileLine = json.loads(line)
        listedFile.append(fileLine)
        top10 = sorted(top10, key=lambda x: (x["user"]["statusesCount"]), reverse = True)
        if fileLine["user"]["statusesCount"] > top10[9]["user"]["statusesCount"]:
            for i in range(len(top10)):
                if top10[i]["user"]["username"] == fileLine["user"]["username"] and fileLine["user"]["statusesCount"] > top10[i]["user"]["statusesCount"]:
                    top10[i] = fileLine
                    specialCase = True
                    break
                elif  top10[i]["user"]["username"] == fileLine["user"]["username"] and fileLine["user"]["statusesCount"] <= top10[i]["user"]["statusesCount"]:
                    specialCase = True
            if specialCase is False:
                top10[9] = fileLine
                

    for p in top10:
        print(p["user"]["username"] + " - " + str(p["user"]["statusesCount"]))
    return top10
 