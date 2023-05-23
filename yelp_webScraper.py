import requests
from bs4 import BeautifulSoup
import pandas as pd

# function to scrape data when keyword, location, num_pages given
def scrape_yelp(keyword, location, num_pages):
    
    # to store scrape data
    businesses  = []
    
    # loop over number of pages  
    for page in range(num_pages):

        # Construct the Yelp search URL
        URL = f"https://www.yelp.com/search?find_desc={keyword}&find_loc={location}&start={page * 10}"

        # Send GET request and parse HTML response
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract business information
        business_elements = soup.find_all(attrs={"data-testid": "serp-ia-card"})
        
        # Iterate over business elements and extract information
        for business_element in business_elements:
            business_name = business_element.find("h3", class_="css-1agk4wl").text
            business_rating = business_element.select('[aria-label*=rating]')[0]['aria-label']
            business_reviewCount = business_element.find(class_="css-chan6m").text
            # check priceRage tag exist
            business_priceRang_tag = business_element.find(class_="priceRange__09f24__mmOuH")
            business_priceRang = "" if business_priceRang_tag is None else business_priceRang_tag.text
            # check location tag exist
            business_location_tag = business_element.find(class_="css-dzq7l1")
            business_location = "" if len(business_location_tag) < 3 else business_location_tag.contents[2].text
            
            # append results to array
            businesses.append({'business_name': business_name, 'business_rating': business_rating, 'business_reviewCount': business_reviewCount, 'business_priceRang': business_priceRang, 'business_location': business_location})#
                        
    return businesses

# Check if the script is being run directly
if __name__ == '__main__':
    # Prompt the user to enter the keyword, location, and number of pages
    keyword = input("Enter the keyword: ")
    location = input("Enter the location: ")
    num_pages = int(input("Enter the Number of pages: "))
            
    scraped_data = scrape_yelp(keyword, location, num_pages)
    
    print(pd.DataFrame.from_dict(scraped_data))