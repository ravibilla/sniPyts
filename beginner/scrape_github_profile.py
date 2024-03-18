# Scrape github profile
#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup as bs 

github_profile = "https://github.com/ravibilla"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"class": "avatar avatar-user width-full border color-bg-default"})["src"]
print(profile_picture)