import requests
import re
import time
from datetime import datetime
import csv
appType = 8
url = "https://www.zhihu.com/billboard"
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers)
#print(resp.text)
html = resp.text
# print(html)
title_list = re.findall(f'<div class="HotList-itemTitle">(.*?)</div>', html, re.S)
#print(title_list)
for index,title in enumerate(title_list):
    print(index+1, title)
cardids = re.findall(f'"cardId":"Q_(.*?)"', html)
for index,cardid in enumerate(cardids):
    print(index+1, cardid)
covers = re.findall(f'<img src="(.*?)"', html ,re.S)
for index,cover in enumerate(covers):
    print(index+1, cover)
urls = []
for cardid in cardids:
    url_i = f'https://www.zhihu.com/question/{cardid}'
    urls.append(url_i)
for index, url in enumerate(urls):
    print(index+1, url)

# htmls = [] # 查询每个热搜的页面下载
PageView = []
up = []
for index, url in enumerate(urls):
    resp1 = requests.get(url,headers=headers)
    html = resp1.text
 #  print(html)
    x = re.search(f'被浏览</div><strong class="NumberBoard-itemValue" title="(.*?)">', html, re.S).group()
    pageview = re.search(r'\d+', x, re.S).group()
    y = re.search(f'"author":(.*?)"name":"(?P<upname>(.*?))"', html, re.S)
    up.append(y.group("upname"))
    print(y.group("upname"))
    time.sleep(1)
    PageView.append(pageview)
    resp1.close()
    print(f"正在爬取第{index+1}条：{pageview}")
datetime = datetime.now()
data = {
    'title': title_list,
    'PageView': PageView,
    'appType': [8 for i in range(50)],
    'beief': ['null' for i in range(50)],
    'data': [datetime for i in range(50)],
    'src': urls,
    'Redirect': [2 for i in range(50)],
    'rank': [i+1 for i in range(50)],
    'cover': covers,
    'up': up
}
headers0 = list(data.keys())
rows = zip(*data.values())
data_length = len(title_list)
with open('zhihu.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers0)
    writer.writerows(rows)
resp.close()
print(PageView)