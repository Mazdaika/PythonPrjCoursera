from functions import fineopen
import re

fh = fineopen("regex_sum_252397.txt")
print sum([int(num) for num in re.findall("[0-9]+", fh.read())])