import requests

url = 'http://123.57.208.119:5001/data/toutiao'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # 在这里处理返回的数据
    print(data)
else:
    # 处理请求失败的情况
    print('请求失败')
