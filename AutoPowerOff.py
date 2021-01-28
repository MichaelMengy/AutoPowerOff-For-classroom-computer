from get_time import getDayOfWeek
from get_time import getHour
from get_time import getMinute
from get_time import getSecond
from schedules import shutdown_now
from schedules import shutdown_warn
from schedules import no_specific
from schedules import run_only_on
from schedules import run_except
from schedules import time_rule
from time import sleep
import schedules
from os import system, truncate
def shutdownWithoutWarning():
    system("shutdown -p -f")
    pass
def shutdownWithWaring():
    system("shutdown -s -t 60")
    pass




#the rules MUST be in the order of the time!!!
OFFTIMES = [
    time_rule(True,10,10,0,shutdown_warn,run_except,[1]),
    time_rule(True,11,55,10,shutdown_warn,no_specific,[]),
    time_rule(True,17,15,30,shutdown_now,no_specific,[]),
    time_rule(True,19,59,0,shutdown_now,no_specific,[])
]





print("System time = " + str(getHour()) + ":" + str(getMinute()) + ":" + str(getSecond())+ " DayOfWeek=" + str(getDayOfWeek()) )
to_execute = time_rule(False,114514,114514,114514,114514,114514,[114514])
for each in OFFTIMES:
    if schedules.check(getHour(),getMinute(),getSecond(),getDayOfWeek(),each) == True:
        to_execute.hh = each.hh
        to_execute.mm = each.mm
        to_execute.ss = each.ss
        to_execute.operation = each.operation
        break
if to_execute.hh == 114514:
    print("NO AVALIABLE RULES TO BE EXECUTED!")
    exit(0)
    pass
print("Shutting down at " + str(to_execute.hh) + ":" + str(to_execute.mm) + ":" + str(to_execute.ss) + "..")
while True:
    sleep(0.2)
    if getHour() == to_execute.hh and getMinute() == to_execute.mm and getSecond() == to_execute.ss :
        
        if to_execute.operation == shutdown_now:
            print("at once")
            shutdownWithoutWarning()
            exit(0)
        elif to_execute.operation == shutdown_warn:
            print("1min")
            shutdownWithWaring()
            exit(0) 
        print("No off comand")
        exit(0)

