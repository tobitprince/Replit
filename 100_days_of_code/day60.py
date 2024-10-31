"""
Your program should:
1. Austomatically work out today's date.
2. Prompt the user to input the name and date of their event (year, month and day).
3. Work out the number of days until the event and output it.
4. If the event is happening today, insert some party emojis.
5. If the event was in the past, sad face emojis and tell the user how many days ago it was
"""
import os
import time
import datetime

def check_date(event, year, month, day):
    """_summary_

    Args:
        event (_type_): _description_
        year (_type_): _description_
        month (_type_): _description_
        day (_type_): _description_

    Returns:
        _type_: _description_
    """
    today = datetime.date.today()
    event_date = datetime.date(year=year, month=month, day=day)
    difference = event_date - today
    difference = abs(difference.days)

    if event_date > today:
        return print(f"The {event} is coming soon. {difference} day(s) to go")
    if event_date < today:
        return print(f"Woii, the {event} imepita. It was {difference} day(s) ago")
    return print(f"{event} is today")

def main():
    """_summary_
    """
    os.system("cls")
    print("Event Countdown Timer". center(45, "*"))
    event = input("Input the event: ").title()
    year = int(input("Input the year: "))
    month = int(input("Input the month: "))
    day = int(input("Input the day: "))
    check_date(event, year, month, day)
    time.sleep(5)

if __name__ == "__main__":
    while True:
        main()
