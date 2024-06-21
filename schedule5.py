

from datetime import date, timedelta

#define function to create date range
#adapted from functions on the web
#can be altered to create list every n number of days by changing 7 to desired skip length
def daterange(start_date, end_date):
     for n in range(0, int((end_date - start_date).days) + 1, 3):
         yield start_date + timedelta(n)
         
#create empty list to store dates
datelist = []
#define start and end date for list of dates
start_dt = date(2020, 1, 30)
end_dt = date(2020, 2, 5)
#append dates to list
for dt in daterange(start_dt, end_dt):
    datelist.append(dt)

print(datelist)
    