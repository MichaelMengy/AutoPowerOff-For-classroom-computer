from get_time import getDayOfWeek
from get_time import getHour
from get_time import getMinute
from get_time import getSecond
import schedules
from os import system
def shutdownWithoutWarning():
    system("shutdown -p -f")
    pass
def shutdownWithWaring():
    system("shutdown -s -t 60")
    pass
