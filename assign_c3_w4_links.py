#Following Links in Python

#In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

#Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah
#Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Ayva.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: O
#Strategy
#The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
#
#

import urllib
import bs4
from functions import fineurlopen
import xml.etree.ElementTree as ET

import re

regex = re.compile("<script>(.*?)</script>", re.DOTALL)

html = fineurlopen("http://python-data.dr-chuck.net/known_by_Fikret.html").read()
html15 = fineurlopen("http://python-data.dr-chuck.net/known_by_Fikret.html").read()
html2 = regex.sub("", html15)
count = raw_input("Enter count: ")
pos = raw_input("Enter position: ")

for i in xrange(0,int(count)):
    soup = bs4.BeautifulSoup(html, "html.parser")
    links = soup.find_all('a')
    print links[int(pos)-1].get_text()
    html = urllib.urlopen(links[int(pos)-1].get("href")).read()


for i in xrange(0,int(count)):
    parsed = ET.fromstring(html2)
    links = parsed.findall(".//a")
    print links[int(pos)-1].text
    html15 = urllib.urlopen(links[int(pos)-1].get("href")).read()
    html2 = regex.sub("", html15)