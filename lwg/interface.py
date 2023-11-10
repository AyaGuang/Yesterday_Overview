# 所有爬虫程序应该上传的数据
class all:
    title = str     #标题
    PageView = int  #浏览量
    appType = int   #平台对应的下标，如抖音：1 百度：2等等
    brief = str     #简介,如果没有就上传空字符串
    date = str      #数据日期时间，用于历史记录功能
    src = str       #跳转链接
    Redirect = int  #跳转方式,1跳转浏览器；2跳转网页。
    rank = int      #本日在本平台的排名

# 视频类应该额外上传的数据
class video:
    cover = str     #封面链接
    duration = int  #视频总时长
    up = str        #视频制作者

# 图文类应该额外上传的数据
class pic:
    cover = str     #封面链接
    up = str        #视频制作者

    