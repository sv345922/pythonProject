import requests
import re

def find_connection():
    url_ = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
    last = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
    res = requests.get(url_)
    result = []
    print(res.text)
    if res.status_code == 200 and 'html' in res.headers['Content-Type']:
        urls = re.findall(r'(?<=<a href=\")[\w\W]+?(?=\">)', res.text)
    for url in urls:
        res = requests.get(url)
        result.extend(re.findall(r'(?<=<a href=\")[\w\W]+?(?=\">)', res.text))
    print("Yes" if last in result else "No")

def find_sites(link, ans):
    """выводит список сайтов из ссылок на странице"""
    link = 'http://pastebin.com/raw/7543p0ns' #input()
    res = requests.get(link)
    pattern = r'''<a .*href=\s*[\"\'](.+?)[\"\']'''
    sites = re.findall(pattern, res.text)
    pattern2 = r'([\w-]+\.)+w{2,4}'
    result = set()
    for elem in sites:
        if "../" in elem[:4]:
            continue
        site = re.search(pattern2, elem)
        if site:
            result.add(site.group())
    result = sorted(result)

    for i in range(len(result)):
        if result[i] != ans[i]:
            print(f"{result[i]} != {ans[i]}")


test_line = """<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">"""
test2 = "http://pastebin.com/raw/7543p0ns"

test2_ans = """adworker.ru
banner.rbc.ru
biztorg.ru
blogi.rbc.ru
cnews.ru
consensus.rbc.ru
conv.rbc.ru
credit.rbc.ru
data.rbc.ru
dict.rbc.ru
drinktime.ru
events.cnews.ru
export.rbc.ru
finolymp.ru
gift.cnews.ru
graph.rbc.ru
magazine.rbc.ru
map.rbc.ru
marketing.rbc.ru
memori.ru
otc-pif.rbc.ru
otc-stock.rbc.ru
pda.rbc.ru
pogoda.rbc.ru
portfolio.rbc.ru
quote-otc.rbc.ru
quote.ru
raiting.rbc.ru
rating.rbc.ru
realty.rbc.ru
redir.rbc.ru
rss.rbc.ru
seminar.rbc.ru
spb.rbc.ru
sport.rbc.ru
static.feed.rbc.ru
stock.rbc.ru
style.rbc.ru
ta.rbc.ru
tata.ru
top.rbc.ru
top100.rambler.ru
turbo.ru
tv.rbc.ru
ug.rbc.ru
ulov-umov.ru
videoarchive.rbc.ru
www.5ballov.ru
www.armd.ru
www.autonews.ru
www.biztorg.ru
www.cnews.ru
www.conf.rbc.ru
www.event.rbc.ru
www.iglobe.ru
www.informer.ru
www.ivd.ru
www.liveinternet.ru
www.m-2.ru
www.nashidengi.ru
www.pochta.ru
www.quote.ru
www.quoterate.ru
www.quotetotal.ru
www.rbc.ru
www.rbc.ua
www.rbcdaily.ru
www.rbcinfosystems.com
www.rbcnews.com
www.rbctv.ru
www.refunder.ru
www.salon.ru
www.seminar.rbc.ru
www.top.rbc.ru
www.turbo.ru
www.turist.ru
www.utro.ru
www.worldclass.ru
zoom.cnews.ru""".split()

test3 = r'''<a href="https://stepic.org/media/attachments/lesson/24472/sample1.html">1</a>
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href= "ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
<a href="../some_path/index.html">
<a href="sas-_0123d.ifmo.ru">
<a target='_top' href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">'''
test3_ans = """mail.ru
neerc.ifmo.ru
redir.rbc.ru
sas-_0123d.ifmo.ru
stepic.org
www.ya.ru
ya.ru""".split()
find_sites(test2, test2_ans)