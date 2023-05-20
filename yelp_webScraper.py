import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_yelp(keyword, location, num_pages):
    
    for page in range(num_pages):
        # URL for the website we gonna scrape
        URL = f"https://www.yelp.com/search?find_desc={keyword}&find_loc={location}&start={page * 10}"
        # request HTML data from the url page
        response = requests.get(URL)
        #response.headers
        #print(response.text)

        soup = BeautifulSoup(response.content, 'html.parser')

        business_elements = soup.find_all(attrs={"data-testid": "serp-ia-card"})
        businesses  = []
        for business_element in business_elements:
            business_name = business_element.find("h3", class_="css-1agk4wl").text.strip()
            business_rating = business_element.select('[aria-label*=rating]')[0]['aria-label']
            business_reviewCount = business_element.find(class_="css-chan6m").text.strip()
            #business_priceRang = business_element.find(class_="priceRange__09f24__mmOuH").text.strip()
            #business_location = business_element.find(class_="css-dzq7l1").contents[2].text.strip()
            #print(business_reviewCount)
            businesses .append({'business_name': business_name, 'business_rating': business_rating, 'business_reviewCount': business_reviewCount})#, 'business_priceRang': business_priceRang, 'business_location': business_location
                        
    return businesses

if __name__ == '__main__':
    keyword = input("Enter the keyword: ")
    location = input("Enter the location: ")
    num_pages = int(input("Enter the Number of pages: "))
            
    scraped_data = scrape_yelp(keyword, location, num_pages)
    
    print(pd.DataFrame.from_dict(scraped_data))