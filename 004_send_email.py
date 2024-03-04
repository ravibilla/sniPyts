# Send email
import os
import random
import smtplib

def send_email():
    user = input("Enter your name >>")
    email = input("Enter your e-mail >>")
    message = (f"Dear {user}, weclome to snipyts")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendmail('&&&&&&&', email, message)
    print("Email sent")

send_email()
