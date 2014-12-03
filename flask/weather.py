# Dommert
# Weather JSON

#Get JSON data from URL
def getjson(jsonurl):

    # Import Modules
    import json
    import urllib2

    # JSON data string
    data = json.load(urllib2.urlopen(jsonurl))
    # Return the JSON cause thats all we care about
    return data

# Date Time Link: http://date.jsontest.com/
# IP Address: http://ip.jsontest.com/

print "------"
mydata = getjson('http://api.openweathermap.org/data/2.5/weather?q=chandler,az')
print mydata
K = mydata['main']['temp']
f = ((K - 273.15) * 1.8) + 33
print "------"
print K
print mydata['name']
print f
