import sqlite3
import datetime
import sys
from downloadstock import DownloadStock
from dateutil.relativedelta import *
from analyzedata import AnalyzeData


def menu(startDate, endDate):
    print "Top 10 Companies with maximum transactional volume: "
    print "1. Daily"
    print "2. Weekly"
    print "3. Monthly"
    print "4. Yearly"
    print "5. Daily using %age"
    print "6. Weekly using %age"
    print "7. Monthly using %age"
    print "8. Yearly using %age"
    print "="*5, "Bottom 10", "="*5
    print "9. Daily"
    print "10. Weekly"
    print "11. Monthly"
    print "12. Yearly"
    print "13. Daily using %age"
    print "14. Weekly using %age"
    print "15. Monthly using %age"
    print "16. Yearly using %age"
    print "Top 10 Companies with maximum Trans Money: "
    print "17. Daily"
    print "18. Weekly"
    print "19. Monthly"
    print "20. Yearly"
    print "21. Daily using %age"
    print "22. Weekly using %age"
    print "23. Monthly using %age"
    print "24. Yearly using %age"
    print "="*5, "Bottom 10", "="*5
    print "25. Daily"
    print "26. Weekly"
    print "27. Monthly"
    print "28. Yearly"
    print "29. Daily using %age"
    print "30. Weekly using %age"
    print "31. Monthly using %age"
    print "32. Yearly using %age"
    print "33. Exit"
    print "Valid date as input are ", startDate.strftime("%d-%m-%Y"), " to ", endDate.strftime('%d-%m-%Y'), "\n"


def getInputForData(choice, startDate, endDate):
    if choice == '1':  # Data for a particular date
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDay(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '2':
        # show data for a particular week
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeek(mondayDate, fridayDate)

    elif choice == '3':
        # Get data for month
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonth(month, endDate.year)

    elif choice == '4':
        # Get data for the whole year
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYear(year)
    elif choice == '5':
        # show data for a day using percentage
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayUsingPercentage(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '6':
        # show data for a particular week using percentage
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekUsingPercentage(mondayDate, fridayDate)
    elif choice == '7':
        # Get data for month using percentage
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthUsingPercentage(month, endDate.year)

    elif choice  == '8':
        # Get data for the whole year using percentage
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearUsingPercentage(year)


    elif choice == '9':
    # Data for a particular date descending
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayDesc(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '10':
        # show data for a particular week descending
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekDesc(mondayDate, fridayDate)

    elif choice == '11':
        # Get data for month descending
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthDesc(month, endDate.year)

    elif choice == '12':
        # Get data for the whole year descending
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearDesc(year)
    elif choice == '13':
        # show data for a day using percentage descending
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayUsingPercentage(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '14':
        # show data for a particular week using percentage descending
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekUsingPercentageDesc(mondayDate, fridayDate)
    elif choice == '15':
        # Get data for month using percentage descending
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthUsingPercentageDesc(month, endDate.year)

    elif choice  == '16':
        # Get data for the whole year using percentage descending
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearUsingPercentageDesc(year)

    elif choice == '17':  # Data for a particular date Trans money
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayTransMoney(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '18':
        # show data for a particular week
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekTransMoney(mondayDate, fridayDate)

    elif choice == '19':
        # Get data for month Trans money
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthTransMoney(month, endDate.year)

    elif choice == '20':
        # Get data for the whole year Trans money
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearTransMoney(year)
    elif choice == '21':
        # show data for a day using percentage Trans money
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayUsingPercentageTransMoney(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '22':
        # show data for a particular week using percentage Trans money
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekUsingPercentageTransMoney(mondayDate, fridayDate)
    elif choice == '23':
        # Get data for month using percentage Trans money
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthUsingPercentageTransMoney(month, endDate.year)

    elif choice  == '24':
        # Get data for the whole year using percentage Trans money
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearUsingPercentageTransMoney(year)


    elif choice == '25':
    # Data for a particular date descending Trans money
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayDescTransMoney(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '26':
        # show data for a particular week descending Trans money
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekDescTransMoney(mondayDate, fridayDate)

    elif choice == '27':
        # Get data for month descending Trans money
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthDescTransMoney(month, endDate.year)

    elif choice == '28':
        # Get data for the whole year descending Trans money
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearDescTransMoney(year)
    elif choice == '29':
        # show data for a day using percentage descending Trans money
        date = raw_input("Enter date to view data for: ")
        date = convertToDateObj(date)
        if False != date and isValidInputDate(date, startDate, endDate):
            print "Showing data for: ", formatDate(date)
            AnalyzeData.getDataForDayUsingPercentageTransMoney(date.date())
        else:
            print "Invalid date provided. Please choose between the specified dates."
            return
    elif choice == '30':
        # show data for a particular week using percentage descending Trans money
        date = raw_input("Enter date for view data for that particular week(first day: monday): ")
        date = convertToDateObj(date)
        if not (False != date and isValidInputDate(date, startDate, endDate)):
            print "Invalid date provided. Please choose between the specified dates."
            return
        else:
            if date.weekday() > 0:
                mondayDate = date + relativedelta(weekday=MO(-1))
                fridayDate = date + relativedelta(weekday=FR(-1))

            else:
                mondayDate = date + relativedelta(weekday=MO)
                fridayDate = date + relativedelta(weekday=FR)

            mondayDate = mondayDate.date()
            fridayDate = fridayDate.date()

            if mondayDate < startDate:
                mondayDate = startDate

            if fridayDate > endDate.date():
                fridayDate = endDate.date()

            print "Showing data for week ", formatDate(mondayDate), "(monday) to", formatDate(fridayDate) ,"friday"

            AnalyzeData.getDataForWeekUsingPercentageDescTransMoney(mondayDate, fridayDate)
    elif choice == '31':
        # Get data for month using percentage descending Trans money
        prompt = "Enter month to view data for(valid months: {0} to {1}): ".format(startDate.month, endDate.month)
        month = int(raw_input(prompt))
        if month > endDate.month or month < startDate.month:
            print "Invalid month provided. Please choose between the specified dates."
        else:
            AnalyzeData.getDataForMonthUsingPercentageDescTransMoney(month, endDate.year)

    elif choice  == '32':
        # Get data for the whole year using percentage descending Trans money
        prompt = "Enter year to view data for (valid choices are: {0} to {1}".format(startDate.year, endDate.year)
        year = int(raw_input(prompt))
        if int(year) > endDate.year or int(year) < startDate.year:
            print "Invalid year provided. Please choose between the specified years."
        else:
            AnalyzeData.getDataForYearUsingPercentageDescTransMoney(year)



def isValidInputDate(date, startDate, endDate):
    date = date.date()
    if date > endDate.date() or date < startDate:
        return False
    else:
        return True


def convertToDateObj(dateStr):
    try:
        return datetime.datetime.strptime(dateStr, '%d-%m-%Y')
    except ValueError:
        print("Incorrect date format given. Try again.")
        return False

def formatDate(date):
    return date.strftime('%d-%m-%Y')

def main():
    date = raw_input("Enter date for which the calculations will be done (DD-MM-YYYY): ")
    try:
        date = datetime.datetime.strptime(date, '%d-%m-%Y').date()
    except ValueError:
        raise ValueError("Incorrect date format given. Exiting")

    if date > date.today():
        print "Future date given. Exiting. "
        sys.exit()

    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)

    dates = []

    delta = yesterday - datetime.datetime.strptime(date.strftime('%d%m%y'), '%d%m%y')

    for i in range(delta.days + 1):
        dates.append(date + datetime.timedelta(i))

    print "Fetching data from ", date.strftime("%d-%m-%Y"), " to ", yesterday.strftime('%d-%m-%Y'), "\n"
    print "This will take a while."

    for d in dates:
        DownloadStock(d)

    choice = ''

    while choice != '33':
        menu(date, yesterday)
        choice = raw_input("Your choice: ")
        getInputForData(choice, date, yesterday)

    raw_input("press any key to exit...")


if __name__ == "__main__":
    main()

