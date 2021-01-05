from bs4 import BeautifulSoup
import requests


def scrape_local():
    with open('index.html', 'r') as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')
        course_cards = soup.find_all('div', class_='card')
        for course_card in course_cards:
            course_name = course_card.h5.text
            course_price = course_card.a.text.split()[-1]
            print(f'{course_name} costs {course_price}')


def scrape_hosted():
    url = 'https://www.timesjobs.com/candidate/job-search.html'
    payload = {
        'searchType': 'personalizedSearch',
        'from': 'submit',
        'txtKeywords': 'Python'
    }
    html_text = requests.get(url, params=payload).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        print(company_name)


if __name__ == "__main__":
    debug = False
    if debug:
        scrape_local()
    else:
        scrape_hosted()
