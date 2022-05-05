from bs4 import beautifulsoup4
import requests
__all__ = [beautifulsoup4, requests]



class Scraper:
    def __init__(self):
        self.content = None
        self.soup =None
        self.samples = None

    def download(self):
        result = requests.get('https://loteria.guru/resultados-loteria-estados-unidos/us-mega-millions/resultados-anteriores-mega-millions-us')
        if result.status_code == 200:
            self.content = result.content
        else:
            raise Exception("Download could not fletch data.")

    def findSoupSamples(self):
        self.soup = BeautifulSoup(self.content, "html.parser")
        self.samples = self.soup.find('div', )