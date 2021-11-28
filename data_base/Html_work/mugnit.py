import pathlib
import re
from urllib.parse import urljoin, urlparse
import requests
headers = {
    "User-Agent": "Naruto Uzumaki v.2",

}

params = {
    "category[]": "fruits_vegetable",
    "format[]": ["mm", "ms"],
}

url = 'https://magnit.ru/promo/'
response = requests.get(url, headers=headers)

pattern = re.compile(r"<div class=\"card-sale__title\"><p>(.*?)</p></div>")

def get_page(url, to_save=False):
    response = requests.get(url)
    if to_save:
        temporary = url.split("/")
        file_path = pathlib.Path(__file__).parent.joinpath(
            f"{temporary[-1] or temporary[-2]}.html"
        )
        with open(file_path, "wb") as file:
            file.write(response.content)
    return response

url = 'https://magnit.ru/promo/'
response = get_page(url)

products = set()
for link in re.findall(pattern, response.text):
    base = urlparse(response.url)
    url = urljoin(response.url, link)
    if base.netloc == urlparse(url).netloc:
        if url not in products:
            _ = get_page(url, to_save=True)
        products.append(url)
