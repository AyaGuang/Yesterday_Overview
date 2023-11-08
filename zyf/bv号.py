import subprocess
import os
import requests
import re
import json
from pprint import pprint

link='https://api.bilibili.com/x/web-interface/wbi/search/type'
data={
    '__refresh__': 'true',
    '_extra':'',
    'context':'',
    'page': '2',
    'page_size': '42',
    'from_source':'',
    'from_spmid': '333.337',
    'platform': 'pc',
    'highlight': '1',
    'single_column': '0',
    'keyword': '日本排放核污水',
    'qv_id': 'V1CWqo1BDx2lwjjQNM3qBhlD5Yd88lLR',
    'ad_resource': '5654',
    'source_tag': '3',
    'gaia_vtoken':'',
    'category_id':'',
    'search_type': 'video',
    'dynamic_offset': '30',
    'web_location': '1430654',
    'w_rid': 'f9c05b28a8554dfd4936df743087681d',
    'wts': '1694425187'
}

headers={
    'referer':'https://www.bilibili.com/video/',
    'cookie': "finger=158939783; buvid3=942BBE8D-D7FB-4454-A483-E1C11686D57E155804infoc; LIVE_BUVID=AUTO2615719148192115; stardustvideo=1; rpdid=|(k|lmJ|RR~u0J'ul~umuR)ku; im_notify_type_406471840=0; CURRENT_FNVAL=80; CURRENT_QUALITY=112; _uuid=49B9C403-6E0C-AEED-F106-EB07E720DA8E77792infoc; blackside_state=0; fingerprint3=1cdc68f9c484657ac6a71df190afb556; sid=arefm2nd; fingerprint=8b41e39ee276d01b2ed70f677e090d9b; buivd_fp=942BBE8D-D7FB-4454-A483-E1C11686D57E155804infoc; fingerprint_s=2cba7720f0fa69a142e39118d29b55b5; bp_article_offset_406471840=474805593736841983; bp_t_offset_406471840=474850961478201127; PVID=1; buvid_fp=942BBE8D-D7FB-4454-A483-E1C11686D57E155804infoc; buvid_fp_plain=6406A16C-F786-4F63-B253-FE49CA5CAEA6143077infoc; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f; DedeUserID=406471840; DedeUserID__ckMd5=b61a313dfd873915; SESSDATA=9a671851%2C1625047384%2C542f9*11; bili_jct=475eaa698b53f2bc408cb650b2e0aaeb; bp_video_offset_406471840=475267392923742025",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.5162 SLBChan/103'
}
response_1=requests.get(url=link,params=data,headers=headers)
for index in response_1.json()['data']['result']:

    bv_id=index['bvid']
    print(bv_id)

