# 所有爬虫程序应该上传的数据
class all:
    title = str     #标题
    PageView = int  #浏览量
    appType = int   #平台对应的下标，如抖音：1 百度：2等等

    src = str       #跳转链接
    Redirect = int  #跳转方式,1跳转浏览器；2跳转网页。
    rank = int      #本日在本平台的排名

# 视频类应该额外上传的数据
class video:
    cover = str     #封面链接
    up = str        #视频制作者

# 图文类应该额外上传的数据
class pic:
    cover = str     #封面链接
    up = str        #视频制作者

    