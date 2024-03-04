# Calculate age
import datetime

def calc_age(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days/365.25)
    print(f"Your age is: {age}")

calc_age(1981, 7, 15)