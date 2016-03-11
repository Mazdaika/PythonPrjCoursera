def fineopen(defaultfile = "mbox-short.txt"):
    fnvalid = False
    fh = None
    while not fnvalid:
        try:
            fname = raw_input("Enter file name: ")
            if fname == "" : return open(defaultfile)
            fh = open(fname)
            fnvalid = True
        except:
            print "Enter a valid file name!"
    return fh