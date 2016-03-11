# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


from functions import fineopen

fh = fineopen()

senders = dict()
for line in fh:
    if not line.startswith("From ") : continue
    temp = line.split()
    senders[temp[1]] = senders.get(temp[1],0) + 1

frequentSender = None
frequentSends = None
for key,value in senders.items():
    if frequentSends:
        if value > frequentSends:
            frequentSends = value
            frequentSender = key
    else:
        frequentSends = value
        frequentSender = key
print frequentSender,frequentSends