from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from lxml import etree

browser = webdriver.Chrome()
url  ='https://www.zhipin.com/changsha/'
browser.get(url)
browser.set_window_size(1800,800)

#寻找输入框输入
browser.find_element(By.CLASS_NAME,'ipt-search').send_keys('客服')
#寻找搜索按钮点击
# browser.find_element(By.CLASS_NAME,'btn-search').click()
#通过Keys方法敲击回车
browser.find_element(By.CLASS_NAME,'btn-search').send_keys(Keys.ENTER)

browser.implicitly_wait(10) #隐性等待

#寻找多个元素
lis = browser.find_elements(By.CLASS_NAME,'job-card-wrapper')
res = []
i=0

for li in lis:
    if i==5:
        break
    i += 1
    li.click()
    browser.implicitly_wait(10)  # 隐性等待
    #获取新页面句柄
    handles = browser.window_handles
    print(len(handles))
    browser.switch_to.window(handles[-1])
    html = browser.page_source #获取当前页面源数据
    tree = etree.HTML(html)
    name = tree.xpath('//div//h1/text()')
    salary = tree.xpath('//span[@class="salary"]/text()')
    job = {'name':name,'salary':salary}
    res.append(job)
    time.sleep(1)
    #关闭当前窗口
    browser.close()
    #句柄切换回首页
    browser.switch_to.window(handles[0])

# time.sleep(10)

print(res)

input()