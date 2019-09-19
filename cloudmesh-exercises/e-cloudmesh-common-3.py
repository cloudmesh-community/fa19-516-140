# fa19-516-140
#This program demonistrate the use of flatdict
#function which been stored in cloudmesh.common.flatdict

from cloudmesh.common.flatdict import FlatDict

#Assigining values to dicts

values = {'Cloudera': {'Address':{'USA':0,'CA': 1,'Palo Alto': 2}}}

# converting nested dicts to a one flat dict that illustrates all levels in one level with delimited keys

flat = flatdict.FlatDict(values)

#calling the flatdict in a key calling loop for each key based in the flat result

for key in flat:
    print (key)
