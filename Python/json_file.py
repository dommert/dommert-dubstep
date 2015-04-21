#! /usr/bin/python

import json
from pprint import pprint

#json_file='a.json' 
json_file='my_cube.json'
cube='1'

json_data=open(json_file)
data = json.load(json_data)
#pprint(data)
json_data.close()

print "Dimension: ", data['cubes'][cube]['dim']
print "Measures:  ", data['cubes'][cube]['meas']