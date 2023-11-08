import jieba
import wordcloud
import imageio
img=imageio.imread('地球.png')
#1.读取弹幕数据
f=open('弹幕.txt',encoding='utf-8')
text=f.read();
#print(text);
#分词，把一句话分割成多个词汇
text_list=jieba.lcut(text)
print(text_list)
#3.列表转成字符串
text_str=' '.join(text_list)
print(text_str)
#4.词云图配置
wc=wordcloud.WordCloud(
    width=500,
    height=500,
    mask=img,
    stopwords={'的','了','吧','啊','是','我','你','他'},
    font_path='msyh.ttc'
)

wc.generate(text_str)
wc.to_file('词云1.png')