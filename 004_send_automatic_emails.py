# Send automatic emails
import os
import random
import smtplib

def automatic_email():
    user = input("Enter your name >>")
    email = input("Enter your e-mail >>")
    message = (f"Dear {user}, weclome to snipyts")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendmail('&&&&&&&', email, message)
    print("Email sent")

automatic_email()
