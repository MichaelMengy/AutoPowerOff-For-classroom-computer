from datetime import datetime as tapi
def getHour() -> int:
    d = tapi.now()
    return int(d.hour)
    pass
def getMinute() -> int:
    d = tapi.now()
    return int(d.minute)
    pass
def getSecond() -> int:
    d = tapi.now()
    return int(d.second)
    pass
def getDayOfWeek() -> int:
    d = tapi.now()
    return int(d.weekday)
    pass
