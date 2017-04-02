import calendar
def daysInYear(year):
	if year%400 :
		return 366#if leep year return 366
	else:
		return 365#if normal year return 365

#return days used once
def calculateDays(day,month,year):
	days=day
	for i in range(1,month+1):
		days=days+calendar.monthrange(year,i)[1]
	return days
#return date [day,month,year] by inserting th total days and current year
def getDate(days,year):
	mDays=calendar.monthrange(year,1)[1]
	month=1
	while True:
		if days <= mDays:
			return [days,month,year]
		else:
			days=days-mDays
			month=month+1
			mDays=calendar.monthrange(year,month)[1]
#return date of The Feast of St. Habakkuk
def getFeastDateNumber(number):
	year=559
	days=calculateDays(14,7,year)
	for i in range(0,number):
		days=days+256
		if days > daysInYear(year):
			year=year+1
			days=days-daysInYear(year-1)
	return getDate(days,year)
date=getFeastDateNumber(10)
print("Day: ",date[0],",Month: ",date[1],",Year: ",date[2])
