#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

from functions import fineopen
import re
fh = fineopen()
hdistr = dict()
for line in fh:
    if not line.startswith("From "): continue
    searchresult = re.search('(\d\d):\d\d:\d\d',line)
    hour = searchresult.group(1)
    hdistr[hour] = hdistr.get(hour,0) + 1
for h,c in sorted([(k,v) for k,v in hdistr.items()]):
    print h, c