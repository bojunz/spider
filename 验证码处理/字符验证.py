from PIL import Image
import numpy as np
import matplotlib
import pytesser3
matplotlib.use('TkAgg')  # You can try other backends like 'Agg', 'Qt5Agg', etc.

import matplotlib.pyplot as plt

img = Image.open('RandCode.png')
img2 = img.convert('L')


print('焦点1',img.getpixel((10, 10)))
print('焦点2',img2.getpixel((10, 10)))

img_np = np.array(img2)
print(img_np)
img_np = img_np.reshape(1, -1)
print(img_np)

# 阈值计算
step = 10
count = {}

for i in range(0, 256, step):
    count[str(i) + str(i + step)] = img_np[(img_np >= i) & (img_np <= i + step)].shape[0]

plt.xlabel('pixel label')
plt.ylabel('count')
plt.bar(range(0, 256, 10), count.values())
plt.show()


avg = 150
width, height = img2.size #获取图片大小
pixel = img2.load()  #获取当前像素值

for x in range(width):
    for y in range(height):
        if pixel[x,y] < avg:
            pixel[x, y] = 0
        else:
            pixel[x, y] = 255

# img.show()
# img2.show()

##降噪

for x in range(1,width-1):
    for y in range(1,height-1):
        count = 0 #统计周边白色像素的个数
        if pixel[x,y-1] > 245: #上
            count+=1
        if pixel[x,y+1] > 245: #下
            count+=1
        if pixel[x-1,y] > 245: #左
            count+=1
        if pixel[x+1,y] > 245: #右
            count+=1
        if pixel[x-1, y - 1] > 245:  # 左上
            count += 1
        if pixel[x-1, y + 1] > 245:  # 左下
            count += 1
        if pixel[x +1, y+1] > 245:  # 右下
            count += 1
        if pixel[x + 1, y-1] > 245:  # 右上
            count += 1

        if count >5:
            pixel[x,y] = 255

img2.show()
code = pytesser3.image_to_string(img2)
print(code)