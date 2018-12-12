import requests
from bs4 import BeautifulSoup
import bs4


def gethtmltext(url):
    try:
        kv = {'user-agent': 'mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillunivlist(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        for tr in soup.find('tr').children:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                ulist.append(tds[0].string)

def printunivlist(ulist, num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = "http://www.ttpaihang.com/vote/rankresult-1089.html"
    html = gethtmltext(url)
    fillunivlist(uinfo, html)
    printunivlist(uinfo, 20)

main()
