import requests_cache
from bs4 import BeautifulSoup
import re

MAIN_DOC_URL = "https://docs.python.org/3/"

if __name__ == "__main__":
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    sidebar = soup.find("div", {"class": "sphinxsidebarwrapper"})
    ul_tags = sidebar.find_all("ul")
    # Перебор в цикле всех найденных списков.
    for ul in ul_tags:
        # Проверка, есть ли искомый текст в содержимом тега.
        if "All versions" in ul.text:
            # Если текст найден, ищутся все теги <a> в этом списке.
            a_tags = ul.find_all("a")
            # Остановка перебора списков.
            break
    # Если нужный список не нашёлся,
    # вызывается исключение и выполнение программы прерывается.
    else:
        raise Exception("Ничего не нашлось")
    # print(a_tags)
    # Список для хранения результатов.
    results = []
    # Шаблон для поиска версии и статуса:
    pattern = r"Python (?P<version>\d\.\d+) \((?P<status>.*)\)"
    # Цикл для перебора тегов <a>, полученных ранее.
    for a_tag in a_tags:
        # Напишите новый код, ориентируясь на план.
        link = a_tag["href"]  # Извлекаем ссылку из тега <a>
        text = a_tag.text.strip()  # Извлекаем текст из тега <a>
        # Попытка извлечь номер версии и статус с помощью регулярного выражения
        match = re.match(pattern, text)
        if match:
            version = match.group("version")
            status = match.group("status")
        else:
            version = text  # Если не соответствует, сохраняем текст полностью
            status = ""  # Статус пустой

        results.append((link, version, status))  # Добавляем кортеж в список результатов
    # Печать результата.
    for row in results:
        print(*row)
