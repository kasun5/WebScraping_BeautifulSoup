import requests
from bs4 import BeautifulSoup
import cfscrape # To bypass cloudfair bot detection

def scrape_indeed(job, location, num_pages):
    base_url = f"https://www.indeed.com/jobs?q={job}&l={location}"
    jobs = []

    # Create a Cloudflare scraper instance
    scraper = cfscrape.create_scraper()

    for page in range(num_pages):
        url = f"{base_url}&start={page * 10}"
        
        # Make the request using the Cloudflare scraper
        response = scraper.get(url)
        
        soup = BeautifulSoup(response.content, 'html.parser')

        job_elements = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for job_element in job_elements:
            title_element = job_element.find('a', class_='jobtitle')
            company_element = job_element.find('span', class_='company')
            location_element = job_element.find('span', class_='location')

            if title_element and company_element and location_element:
                title = title_element.text.strip()
                company = company_element.text.strip()
                location = location_element.text.strip()

                jobs.append({'title': title, 'company': company, 'location': location})

    return jobs

if __name__ == '__main__':
    job = input("Enter the job title: ")
    location = input("Enter the location: ")
    num_pages = int(input("Enter the number of pages: "))

    scraped_jobs = scrape_indeed(job, location, num_pages)

    print("Scraped Jobs:")
    for job in scraped_jobs:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print("---------------------")
