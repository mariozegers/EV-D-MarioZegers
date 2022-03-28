import json
from datetime import datetime
import re

def top10Days():
    tweetsByDay = {}

    for line in open("farmers-protest-tweets-2021-03-5.json" , 'r'):
        fileLine = json.loads(line)
        match = re.search(r'\d{4}-\d{2}-\d{2}', fileLine["date"])
        date = str(datetime.strptime(match.group(), '%Y-%m-%d').date())
        if date in tweetsByDay:
            tweetsByDay[date] += 1
        else:
            tweetsByDay[date] = 1

    top10 = sorted(tweetsByDay.items(), key=lambda x:x[1], reverse=True)[:10]
    for day in top10:
        print(day[0] + ": " + str(day[1]))
    return top10
top10Days()