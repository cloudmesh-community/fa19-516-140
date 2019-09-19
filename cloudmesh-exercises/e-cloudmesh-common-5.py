#This program demonistrate the use of Stopwatch 
#functions which been stored in cloudmesh.common.StopWatch 

from cloudmesh.common.StopWatch import StopWatch
from time import sleep
#starting Stopwatch timer counting
StopWatch.start("mywatch")
#pausing the program for 15 minutes
sleep(15)
#stoping Stopwatch timer counting
StopWatch.stop("mywatch")
#printing the elapsed time between starting and stoping the stopwatch
# (should be quale to the program execution time, 15 second on our demonstration )
print ("Time Elapsed =",StopWatch.get("mywatch"), "(seconds)")
