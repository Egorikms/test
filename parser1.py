import requests
from bs4 import BeautifulSoup as BS


def main():
    
    url = "https://kino-format.ru/films/"
    r = requests.get(url)
    soup = BS(r.text, "html.parser")
    items = soup.find_all("div", {"class": "col-lg-2 col-md-3 col-sm-4 col-6"})

    for item in items:
        name = item.find("h3", {"class": "film-name"}).text.strip()
        janr = item.find("p", {"class": "film-genre"}).text.strip()
        age = item.find("p", {"class": "adult-marker"}).text.strip()
        result = f"{name} | {janr} | {age} \n"
        print(result)
        with open("parser_result.txt", "a", encoding='utf-8') as file:
            file.write(result)


main()






