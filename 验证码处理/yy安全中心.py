from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
import time

from PIL import  Image
from io import BytesIO

driver = webdriver.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")
driver.set_window_size(800,800)
url  ='https://zc.yy.com/reg/udb/reg4udb.do?mode=udb&type=Mobile&appid=1&foreignMB=1&action=3&busiurl=https%3A%2F%2Faq.yy.com&fromadv=lgn&reqDomainList='
driver.get('http://zc.yy.com/reg/udb/reg4udb.do?mode=udb&type=Mobile&appid=1&foreignMB=1&action=3&busiurl=https%3A%2F%2Faq.yy.com&fromadv=lgn&reqDomainList=')


driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="m_mainForm"]/div/div[5]/iframe'))
wait = WebDriverWait(driver,10)
element = wait.until(
    EC.element_to_be_clickable((By.ID,'interActiveWrap'))
)
element.screenshot('verify.png') #对需要验证的图片进行截图保存
driver.switch_to.default_content()

chaojiying = Chaojiying_Client('Timetec','qwe123',957419)

img = Image.open('verify.png')

img_array = BytesIO()
img.save(img_array,format('PNG'))

res = chaojiying.PostPic(img_array.getvalue(),9103)
print(res)

#获得每个点的坐标
pic_list = [[int(j) for j in i.split(',')] for i in res.get('pic_str').split('|')]

#根据返回的坐标依次点击
for pic in pic_list:
    click = ActionChains(driver).move_to_element_with_offset(element,pic[0],pic[1]).click()
    click.perform()
    time.sleep(1)

#找到提交按钮
submit = wait.until(
    EC.element_to_be_clickable(By.CLASS_NAME,'提交按钮的类名')
)
ActionChains(driver).click(submit).perform()

while True:
    pass

