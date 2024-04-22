for i in range(10):
    with open('123.txt','a') as f:
        f.write(f"{str(i)}\n")
        f.close()

import os

a = 'https://so.gushiwen.cn/'
n='RandCode.ashx'

full  = os.path.join(a,'',n)
print(full)

import os


a = 'gushiwen/'  # Remove the leading slash
n = 'RandCode.ashx'

full = os.path.join(a, n)
print(full)