# Send instagram message
#!pip install instabot
from instabot import Bot

Bot.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")
Bot.send_message("YOUR_MESSAGE", ["RECEIVER_USERNAME"])