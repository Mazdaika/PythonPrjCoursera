# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

from functions import fineopen
#execfile("assign7.1.py")
fh = fineopen()
linescount = 0
totalsum = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence"):
        linescount = linescount + 1
        try:
            totalsum = totalsum + float(line[line.find(":")+1:].strip())
        except Exception as ex:
            print ex.message, ex.args

if linescount > 0:
    print "Average spam confidence:", totalsum/linescount
else:
    print "No DSPAM information found"