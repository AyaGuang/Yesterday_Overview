import requests
import re
import json
import string
with open('bv号', 'r') as f:
    i=0
    line = f.readline()
    while line:
        word = line.strip()  # 输入视频号进入网页
        url = 'https://api.bilibili.com/x/player/pagelist?bvid=' + word + '&jsonp=jsonp'  # word就是输入的BV号
        myheaders = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        response = requests.get(url, headers=myheaders)
        getcid = response.content.decode('unicode-escape')  # （line11——line16）编码转换时，先将以Unicode为中间编码，先用decode转换成Unicode编码
        cid = re.findall('"cid":(\d{6,10})', getcid)  # 通过正则表达式获取cid，获取6——10长度的数字,此时是列表
        print(cid[0])
        line = f.readline()


