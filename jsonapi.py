'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py.
The program will prompt for a location,
contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON.
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://python-data.dr-chuck.net/geojson

This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

Washington State University
'''

import urllib
import json
while True:
    addr = raw_input("Enter location: ")
    param = urllib.urlencode({"sensor":"false", "address" : addr})
    try:
        print "Retreiving data for", addr
        result = urllib.urlopen("http://python-data.dr-chuck.net/geojson?%s"%param)
    except Exception as err:
        print "Something's wrong, try again!", err.message, err.args
        continue
    print "Retreived!"
    r = str(result.read())
    print r
    data = json.loads(r)
    if "status" not in data or data["status"] != "OK":
        print "Wrong reply status:", data
        continue
    d = dict()
    print data["results"][0]["place_id"]
    break

