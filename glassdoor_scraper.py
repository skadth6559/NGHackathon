import requests
from bs4 import BeautifulSoup as soup


#returns html data from the website referred to by the url parameter
def request_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405',
           'From': 'pleaseletmein@gmail.com'
    }

    return requests.get(url, headers=headers)

#scrapes the Glassdoor url and returns dictionary containing all job postings for the search query
def scrape(url):
    html = request_data(url)
    bsoup = soup(html.content, 'html.parser')
    
    #Sort through the html to find data
    companies = []
    positions = []
    locations = []
    salaries = []

    for listing in bsoup.findAll('li', {'class':'react-job-listing css-wp148e eigr9kq3'}):
        companies.append(listing.find('div', {'class': 'd-flex justify-content-between align-items-start'}).span.text.strip())
        positions.append(listing.find('div', {'class': 'd-flex flex-column pl-sm css-3g3psg css-1of6cnp e1rrn5ka4'}).findAll('a')[1].text)
        locations.append(listing.find('div', {'class':'d-flex flex-wrap css-11d3uq0 e1rrn5ka2'}).span.text)
        if listing.find('div',{'class':'css-3g3psg pr-xxsm'}) is not None:
            salaries.append(listing.find('div',{'class':'css-3g3psg pr-xxsm'}).span.text.strip())
        else:
            salaries.append("No salary information")

    #Convert all data into dictionary to be returned
    internships = {}
    index = 0

    while index < len(positions):
        internships[positions[index]] = [companies[index], locations[index], salaries[index]]
        index += 1
    
    return internships


url = "https://www.glassdoor.com/Job/internships-jobs-SRCH_KO0,11.htm"
print(scrape(url))