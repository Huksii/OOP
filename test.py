import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.wallpaperflare.com/search?wallpaper=anime+4k&page="
HEADERS = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36"
        }

def get_html(Url, Headers=HEADERS):
    response = requests.get(url=Url, headers=Headers)
    if response.status_code == 200:
        return response.text
    else:
        return f"Ошибка с кодом: {response.status_code}"
    
def processing(html):
    soup = BeautifulSoup(html, "lxml").find("ul", {"class": "gallery"}).find_all("img")
    print(soup)

    all_image = []
    for item in soup:
        img = item.get("data-src")
        all_image.append(img)

    return all_image

def run():
    info = []
    for page in range(1, 11):
        html = get_html(URL + str(page))
        source = processing(html)
        info.extend(source)
        print(f"Page {page} is done")

    with open ("info.json", "w") as file:
        json.dump(info, file, indent=4, ensure_ascii=False)
    
run()