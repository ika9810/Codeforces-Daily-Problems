import requests
from operator import itemgetter
import csv
import random
import datetime
import pytz

# specify the URL to retrieve the data from
url = 'https://codeforces.com/api/problemset.problems'

# create a session object to handle the HTTP requests
session_obj = requests.Session()

# send a GET request to the specified URL with the headers to mimic a web browser
response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

# get the JSON data from the response
#| # | Problem |Rate| Rating | Difficulty | Contest |
data = requests.get(url).json()["result"]
problems = data["problems"]
print(problems)
def rating(difficulty):
    if difficulty <= 1199:
        return {"Rating" : "Newbie", "Difficulty" : difficulty, "Color" : "lightgrey"}
    elif difficulty >= 1200 and difficulty <= 1399:
        return {"Rating" : "Pupil", "Difficulty" : difficulty, "Color" : "brightgreen"}
    elif difficulty >= 1400 and difficulty <= 1599:
        return {"Rating" : "Specialist", "Difficulty" : difficulty, "Color" : "9cf"}
    elif difficulty >= 1600 and difficulty <= 1899:
        return {"Rating" : "Expert", "Difficulty" : difficulty, "Color" : "blue"}
    elif difficulty >= 1900 and difficulty <= 2099:
        return {"Rating" : "Candidate Master", "Difficulty" : difficulty, "Color" : "blueviolet"}
    elif difficulty >= 2100 and difficulty <= 2299:
        return {"Rating" : "Master", "Difficulty" : difficulty, "Color" : "orange"}
    elif difficulty >= 2300 and difficulty <= 2399:
        return {"Rating" : "International Master", "Difficulty" : difficulty, "Color" : "orange"}
    elif difficulty >= 2400 and difficulty <= 2599:
        return {"Rating" : "Grandmaster", "Difficulty" : difficulty, "Color" : "red"}
    elif difficulty >= 2600 and difficulty <= 2999:
        return {"Rating" : "International Grandmaster", "Difficulty" : difficulty, "Color" : "red"}
    elif difficulty >= 3000:
        return {"Rating" : "Legendary Grandmaster", "Difficulty" : difficulty, "Color" : "red"}
Newbie = []
Pupil = []
Specialist = []
Expert = []
Candidate_Master = []
Master = []
International_Master = []
Grandmaster = []
International_Grandmaster = []
Legendary_Grandmaster = []

grade = ["Newbie","Pupil", "Specialist", "Expert", "Candidate Master", "Master", "International Master", "Grandmaster","International Grandmaster", "Legendary Grandmaster"]

print(len(problems))
problem_set = []
for prob in problems:
    try:
        rate = rating(prob["rating"])
        rate["#"] = prob["index"]
        rate["Problem"] = prob["name"]
        rate["Contest"] = "https://codeforces.com/contest/" + str(prob["contestId"])
        #https://codeforces.com/contest/1790/problem/A
        rate["ProblemLink"] = rate["Contest"] + "/problem/" + rate["#"]
        #|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|
        rate["Rate"] = "https://img.shields.io/badge/" + str(rate["Rating"].replace(" ","%20")) + "-" + str(rate["Difficulty"]) +  "-" + rate["Color"]
        problem_set.append(rate)
        color_ = rate["Color"]
        if color_ ==  "lightgrey":
            Newbie.append(rate)
        elif color_ ==  "brightgreen":
            Pupil.append(rate)
        elif color_ ==  "9cf":
            Specialist.append(rate)
        elif color_ ==  "blue":
            Expert.append(rate)
        elif color_ ==  "blueviolet":
            Candidate_Master.append(rate)
        elif color_ ==  "orange":
            if rate["Rating"] == "International Master":
                International_Master.append(rate)
            else:
                Master.append(rate)
        elif color_ ==  "red":
            if rate["Rating"] == "Grandmaster":
                Grandmaster.append(rate)
            elif rate["Rating"] == "International Grandmaster":
                International_Grandmaster.append(rate)
            else:
                Legendary_Grandmaster.append(rate)
    except:
        print(prob)

f = open('Problem_List.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(["Number","index",'Problem', "Rate", "Rating", "Color", 'Difficulty', "Link", "Contest"])
for i in range(len(problem_set)):
    index = problem_set[i]['#']
    Problem = problem_set[i]['Problem']
    Rate = problem_set[i]['Rate']
    Rating = problem_set[i]['Rating']
    Color = problem_set[i]["Color"]
    Difficulty = problem_set[i]["Difficulty"]
    link = problem_set[i]['ProblemLink']
    contest = problem_set[i]["Contest"]
    wr.writerow([i+1,index,Problem,Rate,Rating,Color,Difficulty,link,contest])

grade = [Newbie,Pupil,Specialist,Expert,Candidate_Master,Master,International_Master,Grandmaster,International_Grandmaster,Legendary_Grandmaster]
today_ = []
for j in range(len(grade)):
    try:
        res = random.choice(grade[j])
        today_.append(res)
    except:
        print(j,grade[j])
print(today_,"here")
#Number,index,Problem,Rate,Rating,Color,Difficulty,Link,Contest
#|A|[ABC219_C](https://atcoder.jp/contests/abc219/tasks/abc219_c)|![Rate](https://img.shields.io/badge/9%20Kyu-227-lightgrey)|9 Kyu|227|[https://atcoder.jp/contests/abc219](https://atcoder.jp/contests/abc219)|
#Generate Markdown by Contests

timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
timeformat = f"{timeformat.strftime('(%Y-%m-%d)')}"
dateformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
date = f"{dateformat.strftime('%Y-%m-%d')}"
saveline = []
title = "### 🌟Today's Codeforces Daily Problems " + timeformat

saveline.append(title + '\n')
saveline.append("(Notes: The problems in this contest were curated based on their level of difficulty and listed from Codeforces's existing problems)\n")
saveline.append("\n")
saveline.append("| # | Problem | Rate| Rating | Difficulty | Contest |\n")
saveline.append("|---| ----- | :--------: | :----------: | :----------: | ---------- |\n")

for pro in today_:
    msg = "|"+ pro["#"]+"|["+pro["Problem"]+"]("+pro["ProblemLink"]+")|![Rate]("+ str(pro["Rate"]) + ")|" + pro["Rating"] + "|" + str(pro["Difficulty"]) + "|[" + pro["Contest"] + "]("+ pro["Contest"] +")|\n"
    saveline.append(msg)
    #saveline.append("\n")
f = open('README.md')
lines = f.readlines()
f.close()
with open('./README.md', 'w') as f:
    f.writelines(lines[:6] + saveline)
    f.close()
with open('./archive/'+date+".md", 'w') as f:
    f.writelines(saveline)
    f.close()