from PIL import Image
import io

# 打开图像文件
image = Image.open("cover1.jpg")

# 创建一个BytesIO对象
byte_stream = io.BytesIO()

# 将图像保存到BytesIO对象中
image.save(byte_stream, format='JPGE')

# 获取二进制数据
binary_data = byte_stream.getvalue()

print(binary_data)

# 关闭BytesIO对象
byte_stream.close()
