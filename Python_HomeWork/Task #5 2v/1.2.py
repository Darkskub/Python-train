import re
import calendar

date = str(input("Enter date format YYYY-MM: "))


def calendar(date):
    pattern = re.compile(r"\d{4}-\d{2}")
    if pattern.match(date):
        year, month = map(int, date.split("-"))
        cal = calendar.monthcalendar(year, month)
        for week in cal:
            print(week)
    else:
        print("The date format is incorrect. Please enter the date in YYYY-MM format.")


calendar(date)

phone_number = str(input("Enter a phone number in the format +7-***-***-**-**: "))


def phone_number_check(phone_number):
    pattern = r"^(\+7|7|8)-\d{3}-\d{3}-\d{2}-\d{2}$"
    if re.match(pattern, phone_number):
        print(f"Phone number {phone_number} matches the format.")
    else:
        print(f"Phone number {phone_number} does not match the format.")


phone_number_check(phone_number)
