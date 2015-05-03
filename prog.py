import sqlite3
import datetime
import sys
from downloadstock import DownloadStock


def main():
    conn = sqlite3.connect('SQLite_DB\\stock')
    cursor = conn.cursor()

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

    delta = yesterday - datetime.datetime.strptime(date.strftime('%d%m%y'),'%d%m%y')



    for i in range(delta.days + 1):
        dates.append(date + datetime.timedelta(i))

    print "Fetching data from ", date.strftime("%d-%m-%Y"), " to ", yesterday.strftime('%d-%m-%Y'), "\n"
    print "This will take a while."

    for date in dates:
        DownloadStock(date)



    raw_input("press any key to exit...")

if __name__ == "__main__":
    main()