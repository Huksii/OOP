import json
import requests
from bs4 import BeautifulSoup
from headers import ParSite

# site = ParSite("https://rezka.ag")

class Rezka(ParSite):
    def __init__(self, URL: str) -> None:
        super().__init__(URL)

    def processing(self):
        soup = BeautifulSoup(self.get_html(), "lxml"
            ).find("div",  {"class": "b-content__inline_items"}
            ).find_all("div", {"class": "b-content__inline_item"})
    
        film_informations = []

        for item in soup:
            film_photo = item.find("img").get("src")
            film_title = item.find("div", {"class": "b-content__inline_item-link"}).find("a").text
            film_url = item.find("div", {"class": "b-content__inline_item-link"}).find("a").get("href")
            film_category = item.find("div", {"class": "b-content__inline_item-link"}).find("div").text

            film_informations.append({
                "title": film_title,
                "photo": film_photo,
                "url": film_url,
                "category": film_category,
                })
        
        return film_informations
    
    def create_json(self):
        with open(f"{self.url.strip('https://').split('.')[0]}.json", "w", encoding="utf-8") as f:
            json.dump(self.processing(), f, indent=4, ensure_ascii=False)
        return f"Файл {f.name} успешно создан"

# rezka = Rezka("https://rezka.ag")

# print(rezka.create_json())

class Wallpaper(ParSite):
    def __init__(self, URL: str) -> None:
        super().__init__(URL)
        self.all_image = []
        self.info = []

    def processing(self, html):
        self.all_image.clear()
        soup = BeautifulSoup(html, "lxml").find("ul", {"class": "gallery"}).find_all("img")

        for item in soup:
            img = item.get("data-src")

            self.all_image.append(img)

        return self.all_image
    
    def run_processing(self):
        for page in range(1, 3):
            self.url += str(page)

            html = self.get_html()
            source = self.processing(html)

            self.info.extend(source)
            print(f"Страница {page} готова!")

            self.url = self.url[:62]

        with open("Wallpaper_url.json", "w") as file:
            json.dump(self.info, file, indent=4, ensure_ascii=False)

        return "Анализ сайта завершен!"
    
    def download_img(self):
        print(self.run_processing())

        for image_url in self.info:
            responce = requests.get(image_url)

            with open(f"image/{image_url.split('/')[-1]}", "wb") as image_file:
                image_file.write(responce.content)
            
            print (f"Я скачал фотографию {image_url.split('/')[-1]}")
    
# flare = Wallpaper("https://www.wallpaperflare.com/search?wallpaper=anime+4k&page=")

# flare.download_img()

# print(flare.run_processing())

    