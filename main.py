from bs4 import BeautifulSoup


def main():
    with open('index.html', 'r') as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')
        course_cards = soup.find_all('div', class_='card')
        for course_card in course_cards:
            print(course_card.h5)


if __name__ == "__main__":
    main()
