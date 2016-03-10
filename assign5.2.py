lst = []
smallest = None
biggest = None

while True:
    inp = raw_input("Type in a number: ")
    if inp == "done" : break
    try:
        inp = int(inp)
    except:
        print "Invalid input"
        continue
    lst.append(inp)

for l in lst:
    if biggest is None:
        smallest = l
        biggest = l
    else:
        if l > biggest:
            biggest = l
        if l < smallest:
            smallest = l
print "Maximum is", biggest
print  "Minimum is", smallest