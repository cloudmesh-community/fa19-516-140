# fa19-516-140
#This program demonistrate the use of dotdict 
#functions which been stored in cloudmesh.common.dotdictl 

from cloudmesh.common.dotdict import dotdict

#storing (key:value) fields
data = {"Program": "OK"}
#converting stored (key:value) in a dotict dictionary
data = dotdict(data)

# using value of dotdict as a condition
if data.Program is "OK":
    print("This Program is to Demonstrate DotDict!")
