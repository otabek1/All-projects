import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = (BeautifulSoup(res.text, "html.parser"))
links = soup.select(".storylink")
subtext = soup.select(".subtext")
# print(links, subtext)


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["points"], reverse=True)


def data(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()

# print(title)
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(str(vote[0].getText()).replace(f"points", " "))
        if points > 99:
            hn.append({"title": title, "link": href, "points": points})

    return sort_by_votes(hn)


pprint.pprint(data(links, subtext))
