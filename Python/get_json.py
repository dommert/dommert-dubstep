# Dommert 2014 - MIT Open Source
# Get JSON data from URL
def getjson(jsonurl):

    # Import Modules
    import json
    import urllib2

    # JSON data string
    data = json.load(urllib2.urlopen(jsonurl))
    # Return the JSON cause thats all we care about
    return data