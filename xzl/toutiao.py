import re
import time
import requests
from urllib.request import urlopen
appType = 7
url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
html = resp.text
# print(html)
title_list = re.findall(f'"Title":"(.*?)",', html, re.S)
title_list.pop()
urls = re.findall(f'"Url":"(.*?)/\?', html, re.S)
for index, title in enumerate(title_list):
    print(index+1, title)
for index, url in enumerate(urls):
    print(index+1, url)
PageView = []
# htmls = []
headers1 = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
'Cookie':
'tt_webid=7301724020972537385; local_city_cache=%E7%A6%8F%E5%B7%9E; csrftoken=d83a41990ba0b056f57fabcd0019ea5b; s_v_web_id=verify_lozyvmt0_vVxjU1cM_XbAN_4q0V_BthZ_CzAhAH04oXwE; _ga=GA1.1.858410103.1700065121; msToken=ERxS54lvFtIzJZ_G8f0dWZFaMwgFVjtT6oGrx5Mh3WZ0O44vO-IxciJ76rgKAbj-ZELe86eK5zPJp0vhW8IDl3BM_6xRlFiK4IU-WyG3; ttwid=1%7C6ZtxPrEY8NdRaPqMsqaqnSqIjfgB8jS-bJ6TKruhmX8%7C1700068577%7C93f4f459cd8175a6088052be9b9f0901aa6f2661306399734b2a3b0666c63ad6; _ga_QEHZPBE5HH=GS1.1.1700065121.1.1.1700068576.0.0.0; tt_scid=ePWSVHAzd.CWVzfk1QNDgulkV3s6-GvmcC9bwpf8mOUoUDfc81uIq19wRwi-tTNM5f40'
}
for index, url in enumerate(urls):
    resp1 = requests.get(url, headers=headers1)
    resp1.encoding = 'utf-8'
    html1 = resp1.text
    time.sleep(1)
    #print(html1)
    x = re.search(f'阅读量<span class="num">(?P<num>(.*?))</span>(?P<dw>(.*?))</span>', html1, re.S)
    PageView.append(x.group("num")+x.group("dw"))
    print(index)
    resp1.close()
resp.close()
print(PageView)

# 因为最后一个放的是置顶项，所以要调整一下位置

# length = len(title_list)-1 # 最大下标
# print(length)
# top = title_list[length]
# for i in range(length, 0, -1):
#     title_list[i] = title_list[i-1]
# title_list[0] = top