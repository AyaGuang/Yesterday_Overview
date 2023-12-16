from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pickle
import time
import os
import csv
import re
import json
import sys
import tempfile
import shutil

def load_cookies(driver, cookies_file):
    if os.path.exists(cookies_file):
        with open(cookies_file, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        return True
    return False
def manual_login(driver, cookies_file):
    input("请登录，登录成功跳转后，按回车键继续...")
    save_cookies(driver, cookies_file)  # 登录后保存cookie到本地
    print("程序正在继续运行")
def save_cookies(driver, cookies_file):
    with open(cookies_file, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)



def main():
    global temp_dir
    # 代码文件所在的文件夹内创建一个新的文件夹，作为缓存目录。如果想自行设定目录，请修改下面代码
    current_folder = os.path.dirname(os.path.abspath(r'C:\Users\陌冼\Desktop\软工\团队项目\β冲刺\代码\bilibili\buffer'))
    temp_dir = tempfile.mkdtemp(dir=current_folder)

    # 设置Chrome浏览器参数
    chrome_options = Options()
    # 将Chrome的缓存目录设置为刚刚创建的临时目录
    chrome_options.add_argument(f'--user-data-dir={temp_dir}')
    chrome_options.add_argument('--disable-plugins-discovery')
    chrome_options.add_argument('--mute-audio')
    # 开启无头模式，禁用视频、音频、图片加载，开启无痕模式，减少内存占用
    # chrome_options.add_argument('--headless')  # 开启无头模式以节省内存占用，较低版本的浏览器可能不支持这一功能
    # chrome_options.add_argument("--disable-plugins-discovery")
    # chrome_options.add_argument("--mute-audio")
    # chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # chrome_options.add_argument("--incognito")
    # 禁用GPU加速，避免浏览器崩溃
    chrome_options.add_argument("--disable-gpu")

    # 首次登录获取cookie文件
    cookies_file = 'cookies.pkl'
    print("测试cookies文件是否已获取。若无，请在弹出的窗口中登录微博账号，登录完成后，窗口将关闭；若有，窗口会立即关闭")
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    driver.get('https://weibo.com/')
    if not load_cookies(driver, cookies_file):
        manual_login(driver, cookies_file)

    with open('video_list.txt', 'r', encoding='utf-8') as f:
        video_urls = f.read().splitlines()
    print('video_urls:')
    print(video_urls)
    for url in video_urls:
        print(f'开始爬取视频：先会不断向下滚动至页面最底部，以加载全部页面。对于超大评论量的视频，这一步会相当花时间，请耐心等待')
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup)
        time.sleep(3)
        link_node = soup.select_one('.from>a')
        # print("link_node")
        # print(link_node)
        href=link_node.get('href')
        #进入href爬取视频
        driver.get('https:'+href)
        time.sleep(2)
        for i in range(4):
            js = 'window.scrollBy(0,500)'
            driver.execute_script(js)
            time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        print(soup)
        comments_list=soup.select('div .text>span')
        with open('wbcomment.txt', 'w', encoding='utf-8') as f:
            for comment in comments_list:
                print(comment)
                print(comment.text)
                f.write(comment.text)
                f.write('\n')
        f.close()
        # time.sleep(2000)
    driver.quit()
if __name__ == '__main__':
    main()