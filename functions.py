def fineopen():
    fnvalid = False
    fh = None
    while not fnvalid:
        try:
            fname = raw_input("Enter file name: ")
            fh = open(fname)
            fnvalid = True
        except:
            print "Enter a valid file name!"
    return fh