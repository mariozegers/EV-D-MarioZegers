import json
from datetime import datetime
import re

def top10Hashtags():
    hashtags = {}

    for line in open("farmers-protest-tweets-2021-03-5.json" , 'r'):
        fileLine = json.loads(line)
        txt = fileLine["content"]
        words = re.findall(r"#(\w+)", txt)
        for word in words:
            if word in hashtags:
                hashtags[word] += 1
            else:
                hashtags[word] = 1

    top10 = sorted(hashtags.items(), key=lambda x:x[1], reverse=True)[:10]
    for hashtag in top10:
        print(hashtag[0] + ": " + str(hashtag[1]))
    return top10

top10Hashtags()