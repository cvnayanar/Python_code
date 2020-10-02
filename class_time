# Create a Time class and initialize it with hours and minutes.
# 1. Make a method addTime which should take two time object and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method displayTime which should print the time.
# 3. Make a method DisplayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class time():
    def __init__(self,hours,min):
        self.hours=hours
        self.minute=min

    def addTime(t1,t2):
        _add_hours=t1.hours+t2.hours
        _add_min = t1.minute+t2.minute
        if _add_min > 60:
            _add_hours+=_add_min//60
            _add_min =_add_min % 60
        print(_add_hours,"hours",_add_min,"minute")

    def displayTime(self):
        pass


a=time(2,45)
b=time(1,30)

c=time.addTime(a,b)
