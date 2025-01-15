from urllib.parse import urljoin
import requests_cache
from bs4 import BeautifulSoup

WHATS_NEW_URL = "https://docs.python.org/3/whatsnew/"

if __name__ == "__main__":
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = "utf-8"
    # Создание "супа".
    soup = BeautifulSoup(response.text, features="lxml")

    # Шаг 1-й: поиск в "супе" тега section с нужным id. Парсеру нужен только
    # первый элемент, поэтому используется метод find().
    main_div = soup.find("section", attrs={"id": "what-s-new-in-python"})

    # Шаг 2-й: поиск внутри main_div следующего тега div с классом toctree-wrapper.
    # Здесь тоже нужен только первый элемент, используется метод find().
    div_with_ul = main_div.find("div", attrs={"class": "toctree-wrapper"})

    # Шаг 3-й: поиск внутри div_with_ul всех элементов списка li с классом toctree-l1.
    # Нужны все теги, поэтому используется метод find_all().
    sections_by_python = div_with_ul.find_all("li", attrs={"class": "toctree-l1"})

    # Печать первого найденного элемента.
    # print(sections_by_python[0].prettify())
    for section in sections_by_python:
        version_a_tag = section.find("a")

        # Вставьте этот код в конце цикла вместо строчки print(version_a_tag).
        href = version_a_tag["href"]
        version_link = urljoin(WHATS_NEW_URL, href)
        print(version_link)