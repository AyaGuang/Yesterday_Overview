import requests
from lxml import etree
import pandas as pd

url="https://tophub.today/n/KqndgxeLl9"
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69'
}
res=requests.get(
    url=url,
    headers=headers
)

html=etree.HTML(res.text)
trs=html.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr')

def getfirsttext(list):
    """
    返回列表中第一个元素
    :return:
    """
    try:
        return list[0].strip()
    except:
        return ""

hot_info = {
    'rank':[],
    'title':[],
    'src':[],
    'cover':[],
    'up':[],
    'PageViews':[],
    'comments':[]
}
# file=open("新微博热搜top50.txt",mode="w",encoding="utf-8")
for tr in trs:
    id=getfirsttext(tr.xpath('./td[1]/text()'))[0:-1]
    title=getfirsttext(tr.xpath('./td[2]/a/text()'))
    play=getfirsttext(tr.xpath('./td[3]/text()'))
    # link= "https://tophub.today"+getfirsttext(tr.xpath('./td[2]/a/@href'))
    link= "https://s.weibo.com/weibo?q="+title
    # hot_info.append((id,title,play,link))
    print(id, title, play, link)
    hot_info['rank'].append(id)
    hot_info['title'].append(title)
    hot_info['src'].append(link)
    hot_info['cover'].append('')
    hot_info['up'].append('')
    hot_info['PageViews'].append('')
    hot_info['comments'].append('')
#     file.write(str(id)+","+title+","+str(play)+","+link+"\n")
# file.close()
save=pd.DataFrame(hot_info)
save.to_csv("./微博热搜top50.csv",index=False,encoding='utf_8_sig')