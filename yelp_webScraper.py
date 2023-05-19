import requests
from bs4 import BeautifulSoup

# URL for the website we gonna scrape
URL = "https://www.yelp.com/search?find_desc=&find_loc=Oklahoma+City%2C+OK"
# request HTML data from the url page
response = requests.get(URL)
#response.headers
#print(response.text)

soup = BeautifulSoup(response.content, 'html.parser')

elements = soup.find_all("h3", class_="css-1agk4wl")

for element in elements:
    title_element = element.text
    print(title_element)
    print()
    