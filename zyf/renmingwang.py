from selenium import webdriver
from bs4 import BeautifulSoup
import base64
import time
import csv
import pandas as pd
import numpy as np


# 创建一个Selenium的webdriver对象，这里以Chrome为例
driver = webdriver.Chrome()

# 访问人民网热点页面
driver.get('http://www.people.com.cn/GB/59476/index.html')

# 等待页面加载完成
time.sleep(5)

# 获取页面源代码
html = driver.page_source

# 创建BeautifulSoup对象
soup = BeautifulSoup(html, 'html.parser')
# print("soup")
# print(soup)
# 查找所有的热点元素
hot_elements = soup.select('li')
# 提取热点的详细信息[]
hot_info = {
    'rank':[],
    'title':[],
    'src':[],
    'cover':[],
    'up':[],
    'PageViews':[],
    'comments':[]
}
rank=0
for elem in hot_elements:
    rank=rank+1
    title = elem.select_one('a').text  # 热点标题
    url = elem.select_one('a')['href']  # 热点链接
    # hot_info.append((rank,title, url))
    hot_info['rank'].append(rank)
    hot_info['title'].append(title)
    hot_info['src'].append(url)
    hot_info['cover'].append('')
    hot_info['up'].append('')
    hot_info['PageViews'].append('')
    hot_info['comments'].append('')

# 打印视频的详细信息
for info in hot_info:
    print(info)


# 关闭webdriver对象
driver.quit()

#  写入csv文件
save=pd.DataFrame(hot_info)
save.to_csv("renmingwang.csv",index=False,encoding='utf_8_sig')