#This program demonistrate the use of banner,HEADING
# and VERBOSE functions which been stored in cloudmesh.common.util & cloudmesh.common.debug
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

#createing class for calling object head_exec which calls HEADING() function
class Heade(object):
    def head_exec():
        HEADING("Hello This is a HEADER Demonstration\n")
#createing class for calling object banne_exec which calls banner() function
class Banne(object):
    def banne_exec():
        banner("Hello This is a BANNER Demonstration\n")
#createing class for calling object verbo_exec which calls VERBOSE() function
class Verbo(object):
    def verbo_exec():
        i={"Hello This is a ":"VERBOSE Demonstration\n"}
        VERBOSE(i)
#poulating classes and calling functions        
b=Banne.banne_exec()
h=Heade.head_exec()
v=Verbo.verbo_exec()
