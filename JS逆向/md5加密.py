from hashlib import md5

def md5_sign(data):
    md = md5()
    md.update(data.encode()) #设置编码格式
    return md.hexdigest() #获取加密的数据

sign = md5_sign(input('请输入你要加密的字符'))
print(sign, len(sign))

'''
i: spider
from: auto
to: 
dictResult: true
keyid: webfanyi
sign: f3d6b2adb151818152589f2571495a77
client: fanyideskweb
product: webfanyi
appVersion: 1.0.0
vendor: web
pointParam: client,mysticTime,product
mysticTime: 1703487465046
keyfrom: fanyi.web
mid: 1
screen: 1
model: 1
network: wifi
abtest: 0
yduuid: abcdefg'''