import requests
import re
with open('cid', 'r') as f0:
    line = f0.readline()
    while line:
        cid = line.strip()  # 输入视频号进入网页
        url='https://api.bilibili.com/x/v1/dm/list.so?oid='+cid
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.5162 SLBChan/103'
        }
        response=requests.get(url=url,headers=headers)
        response.encoding=response.apparent_encoding
        print(response.text)
        data_list=re.findall('<d p=".*?">(.*?)</d>',response.text)
        for index in data_list:
            with open('弹幕.txt',mode='a',encoding='utf-8') as f:
                f.write(index)
                f.write('\n')
            print(index)
        line=f0.readline()