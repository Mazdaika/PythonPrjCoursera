import re
import json
import random

# c:\python27\python sandbox.py


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

def wait_key():
    import msvcrt
    result = msvcrt.getch()
    if result == "z": quit()
    return result

fh = open("quiz.json")
f = fh.read()
j = json.loads(f)
qn = random.choice(xrange(0,19))
print qn,j["Q"+str(qn)]["text"]
print "[1] - {0}".format(j["Q"+str(qn)]["variants"]["A"])
print "[2] - {0}".format(j["Q"+str(qn)]["variants"]["B"])
print "[3] - {0}".format(j["Q"+str(qn)]["variants"]["C"])
print "[4] - {0}".format(j["Q"+str(qn)]["variants"]["D"])
k = wait_key()
if k == "1":
    k = "A"
elif k == "2":
    k = "B"
elif k == "3":
    k = "C"
elif k == "4":
    k = "D"
if j["Q"+str(qn)]["answer"][0].encode("utf-8") == k:
    print "vic!"
else:
    print "lose"