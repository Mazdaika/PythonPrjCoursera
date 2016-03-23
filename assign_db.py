"""
This application will read the mailbox data (mbox.txt) count up the number email messages per organization
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop,
it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number
of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
"""

import sqlite3
import urllib
import os.path
import re

def create_txt():
    try:
        url = urllib.urlopen("http://www.pythonlearn.com/code/mbox.txt")
        fh = open("mbox.txt", mode="w")
        fh.writelines(url)
        print "File retrieved"
        url.close()
        fh.close()
    except:
        print "Error!"

def prepare_db():
    connct = sqlite3.connect("mailbox.sqlite")
    cur = connct.cursor()
    cur.execute("DROP TABLE IF EXISTS Counts")
    cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
    connct.commit()
    connct.close()

def find_domain(str=""):
    domain = re.findall("From\s.+?@(\S+)\s", str)
    if len(domain) > 0:
        return domain[0]
    else:
        return None

if not os.path.isfile("mbox.txt"):
    create_txt()
    print "File created"
else:
    print "File exists"

prepare_db()

fh = open("mbox.txt", mode="r")
connct = sqlite3.connect("mailbox.sqlite")
cur = connct.cursor()

i = 0
for line in fh:
    i = i + 1
    organization = find_domain(line.strip())
    if organization is None: continue
    print organization
    cur.execute("SELECT COUNT(*) FROM Counts WHERE org= ? ", (organization, ))
    row = cur.fetchone()
    if row[0] == 0:
        cur.execute("INSERT INTO Counts (org, count) VALUES (? , 1)", (organization, ))
    else:
        cur.execute("UPDATE Counts SET count=count+1 WHERE org = ?", (organization, ))


connct.commit()
connct.close()



