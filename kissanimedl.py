'''
Name: Jason Le
Email: le.kent.jason@gmail.com
Github: jQwotos
'''

import cfscrape, os, re
from bs4 import BeautifulSoup
baseURL = 'https://kissanime.to'
username = 'Naal1933'
password = 'Naal1933'
loginURL = baseURL + '/Login'
searchURL = baseURL + '/Search/Anime'
acceptableQualities = ["1920x1080.mp4", "1280x720.mp4", "854x480.mp4", "640x360.mp4", "960x720.mp4", "480x360.mp4"]

class Scraper:
    def __init__(self):
        self.scraper = cfscrape.create_scraper()

        login_data = dict(username=username, password=password, next="/")
        self.scraper.post(loginURL, data=login_data, headers={"Referer": "https://myanimelist.net"})

    def Search(self, query = "Sword art online"):
        data = dict(keyword=query)
        resultPage = BeautifulSoup(self.scraper.post(searchURL, data=data, headers={"Referer": baseURL}).content, 'html.parser')
        return resultPage
        table = resultPage.findAll('table', {"class": "listing"})
        data = []
        for row in table.findAll("tr"):
            if 'head' not in row.get('class') and 'height: 10px' not in row.get("style"):
                link = row.get("href")
                title = row.text()
                data.append({"title": title,
                             "link": link})
        return data


    def GetEpisodeLinks(self, link):
        resultPage = BeautifulSoup(self.scraper.get(link).content, 'html.parser')
        vids = []

        for row in resultPage.findAll(attrs={'title' : re.compile("^Watch anime")}):
            link = row.get("href")
            title = row.text
            vids.append({'name': title, 'link': link})

        return vids

    def GetMP4(self, link):
        vids = []
        episodePage = BeautifulSoup(self.scraper.get(baseURL + link).content)
        for l in episodePage.find_all("a"):
            if str(l.text) in acceptableQualities:
                mp4Link = l.get("href")
                return mp4Link

    def Download(self, link, name, destination="Downloads"):
        if not os.exists(destionation):
            os.mkdir(destination)
        os.chdir(destination)
        download_request = self.scraper.get(link, timeout=30, stream=True)
        with open(name + ".tmp", 'wb') as f:
            for chunk in download_request.iter_content(1024 * 1024):
                f.write(chunk)
            os.rename(name + ".tmp", name + ".mp4")
