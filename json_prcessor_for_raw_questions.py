import re
import json

def process_data():
    fh = open("quiz_raw.txt")
    f = fh.read()
    fh.close()

    print f
    quests =  re.findall("Q\s\d+\s:.+?Answer\s:\s.", f)
    dq = {}
    itr = 1
    for q in quests:
        dq["Q"+str(itr)]={}
        dq["Q"+str(itr)]["text"] = re.findall(":\s(.+?\?)", q)[0]
        fa = re.findall("\sA:\s(.+?)\sB:\s(.+?)\sC:\s(.+?)\sD:\s(.+?)\sAnswer",q)

        dq["Q"+str(itr)]["variants"] = {}
        dq["Q"+str(itr)]["variants"]["A"] = fa[0][0]
        dq["Q"+str(itr)]["variants"]["B"] = fa[0][1]
        dq["Q"+str(itr)]["variants"]["C"] = fa[0][2]
        dq["Q"+str(itr)]["variants"]["D"] = fa[0][3]

        dq["Q"+str(itr)]["answer"] = re.findall("Answer\s:\s([A-D])",q)
        itr = itr +1

    j = json.dumps(dq, indent=4)
    fw = open("quiz.json", mode='w')
    fw.write(j)
    fw.close()