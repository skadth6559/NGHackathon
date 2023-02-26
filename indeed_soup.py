import urllib3
import requests

from bs4 import BeautifulSoup

def getData(url):
    r = requests.get(url)
    return r.content

def html_code(url):
    content = getData(url)
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def parse(soup):
    jobs = {}
    result = soup.find_all('a', attrs={'class':"chakra-link css-tjgyl0"})

    section = soup.find('ul', attrs={'id':"job-list"})
    for job in section.children:
        job_name = job.find_next('a', attrs={'class':'chakra-link css-tjgyl0'})
        company = job.find_next('span', attrs={'data-testid':'companyName'})
        location = job.find_next('span', attrs={'data-testid':'searchSerpJobLocation'})
        salary = job.find_next('p', attrs={'class':'chakra-text css-1ejkpji'}) # sometimes, the salary does not exist
        jobs[job_name.get_text()] = [company.get_text(), location.get_text(), "No Salary Information" if salary is None else salary.get_text()]
    
    return jobs

def main():
    # to be implemented
    return None

html = html_code("https://www.simplyhired.com/search?q=internship&l=MD")
# print(html)
print(parse(html))