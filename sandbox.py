dictionary = dict({"one":1,"two":2, "three":3, "four":3})

biggest = None
for value in dictionary.values():
    if not biggest or value > biggest:
        biggest = value

print "Dictionary contents", dictionary
print "The biggest value:", biggest
print "The biggest value position in the list of values:", dictionary.values().index(biggest)
print "Key with the biggest value:", dictionary.keys()[dictionary.values().index(biggest)]