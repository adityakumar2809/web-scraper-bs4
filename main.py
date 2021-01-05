from bs4 import BeautifulSoup
import requests
import textwrap


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
        published_date = job.find('span', class_='sim-posted').span.text
        if published_date == 'Posted few days ago':
            company_name = job.find(
                'h3',
                class_='joblist-comp-name'
            ).text.strip()

            skills = [
                x.strip() for x in job.find(
                    'span',
                    class_='srp-skills'
                ).text.split(',')]

            job_url = job.header.h2.a['href']

            output_str = f'''
                          Company Name: {company_name}
                          Skills Required: {', '.join(skills)}
                          More info: {job_url}
                          '''

            print(textwrap.dedent(output_str))


if __name__ == "__main__":
    debug = False
    if debug:
        scrape_local()
    else:
        scrape_hosted()
