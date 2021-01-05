from bs4 import BeautifulSoup


def main():
    with open('index.html', 'r') as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')
        courses_html_tags = soup.find_all('h5')


if __name__ == "__main__":
    main()
