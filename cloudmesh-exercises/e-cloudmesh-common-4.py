# fa19-516-140
#This program demonistrate the use of Shell  
#functions which been stored in cloudmesh.common.Shell

from cloudmesh.common.Shell import Shell

#assigning command ls -ltr value to i identifier

i=Shell.ls('-ltr')

#prinitng the result of the command 

print(i)
