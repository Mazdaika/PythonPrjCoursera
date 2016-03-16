import urllib

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

def fineurlopen(defaultvalue="http://python-data.dr-chuck.net/known_by_Fikret.html"):
    urlh = None
    while True:
        url = raw_input("Enter url:")
        if url == "" :
            urlh = urllib.urlopen(defaultvalue)
            break
        try:
            urlh = urllib.urlopen(url)
            break
        except Exception as err:
            print "Enter a valid url!\n" + err.message
    return urlh