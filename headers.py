import requests

class ParSite:
    def __init__(self, URL: str) -> None:
        self.url = URL
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36"
        }

    def get_html(self):
        responce = requests.get(self.url, headers=self.headers)
        if responce.status_code == 200:
            html = responce.content.decode('utf-8')
            return html
        else:
            raise Exception(f"Не удалось подключиться: {responce.status_code}")
        
    def __str__(self) -> str:
        return f"Это класс ParSite: {self.url}"