# python datetime


# import the datetime module and display the current date and time
import datetime
#help(datetime)

today = datetime.date.today()   # get the today today
print(today)

now = datetime.datetime.now()  # get current date & time
print(now)

t = datetime.datetime.now().time()   # get only time
print(t)

mydate = datetime.date(2020, 2, 10)
print(mydate)



