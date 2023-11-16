from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


# 创建一个Selenium的webdriver对象，这里以Chrome为例
driver = webdriver.Chrome()

# 访问B站热搜榜页面
driver.get('https://www.bilibili.com/ranking')

# 等待页面加载完成
time.sleep(5)

# 获取页面源代码
html = driver.page_source

# 创建BeautifulSoup对象
soup = BeautifulSoup(html, 'html.parser')
# print("soup")
# print(soup)
# 查找所有的视频元素
video_elements = soup.select('li.rank-item')
# 提取视频的详细信息[排名，标题，视频链接，图片链接，作者名，播放量，评论数]
videos_info = {
    'rank':[],
    'title':[],
    'src':[],
    'cover':[],
    'up':[],
    'PageViews':[],
    'comments':[]
}

for elem in video_elements:
    rank = elem.select_one('span').text  # 视频排名
    title = elem.select_one('a.title').text  # 视频标题
    url = 'https:' + elem.select_one('a.title')['href']  # 视频链接
    image_url = 'https:'+elem.select_one('img')['data-src']  # 视频图片链接
    detail = elem.select('span.data-box')
    auther=detail[0].text.strip()   # 作者名
    views=detail[1].text.strip()    # 播放量
    comments=detail[2].text.strip()  # 评论数
    videos_info['rank'].append(rank)
    videos_info['title'].append(title)
    videos_info['src'].append(url)
    videos_info['cover'].append(image_url)
    videos_info['up'].append(auther)
    videos_info['PageViews'].append(views)
    videos_info['comments'].append(comments)


# # 打印视频的信息
# print(videos_info['rank'])
# print(videos_info['title'])



# 关闭webdriver对象
driver.quit()

#  写入csv文件
save=pd.DataFrame(videos_info)
save.to_csv("bilibili.csv",index=False,encoding='utf_8_sig')