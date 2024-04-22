from PIL import Image
'''
#创建图片
Img = Image.new('RGB',(400,400),(255,155,0))

#保存图片
Img.save('red.png')
'''

'''
#读取图片
img = Image.open('red.png')
#img.show()

#裁剪图片
img = Image.open('rose.png')
sepal = img.crop((250,40,650,400)) #左上角坐标以及右下角坐标
bg = Image.open('red.png')
bg.paste(sepal,(0,0)) #把裁剪出的图片粘贴到橙色背景上
bg.show()

R,G,B = bg.split()
print(R,G,B)'''

#模式转换
img = Image.open('rose.png')
img2 = img.convert('L')
#img.show()

#获取每个像素点的RGB值
# print(list(img.getdata()))
#获取指定像素点
print(img.getpixel((10,10)))

