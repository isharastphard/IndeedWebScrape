from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.indeed.com/jobs?q=data%20analyst%20entry%20level&l=New%20York%2C%20NY&vjk=84851f5a8b45a373').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ ='job_seen_beacon')
sep = 'html'

def find_jobs():
    for index, job in enumerate(jobs):
        job_title = job.find('div', class_ = 'heading4 color-text-primary singleLineTitle tapItem-gutter').text #prints just the role name
        if "new" in job_title: #looks for new listings 
            company_name = job.find('span', class_ = 'companyName').text 
            location_data = job.find('div', class_ = 'companyLocation').text #where the company is located
            try:
                related_jobs = job.find('span', class_ = 'mat').a['href']
            except (AttributeError, KeyError):
                continue
            with open(f'C:\\Users\\Ishar\\Desktop\\webscrape\\{index}.csv', 'w') as f:
                f.write(f"Company Name: {company_name} \n")
                f.write(f"Job Title: {job_title} \n")
                f.write(f"Company Location: {location_data} \n")
                f.write(f"All Postings By {company_name}: https://www.indeed.com{related_jobs} \n")
            print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 12
        print(f"Waiting {time_wait} hours...")
        time.sleep(360*time_wait)
