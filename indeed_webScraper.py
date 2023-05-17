# import required packages
import requests
from bs4 import BeautifulSoup

# URL for the website we gonna scrape
URL = "https://au.indeed.com/jobs?q=data+science&l=&from=searchOnHP&vjk=30ad83d0bd66e8ee"
# request HTML data from the url page
page = requests.get(URL)

