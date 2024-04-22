from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.set_window_size(1800,800)

browser.get('https://www.baidu.com')

'''
隐性等待和显性等待都存在时，超时时间取二者中较大的
browser.implicitly_wait(5)
WebDriverWait(browser,10)'''

wait = WebDriverWait(browser,10)
#判断当前页面是否完全等于预期字符串
print(wait.until(EC.title_is('百度一下，你就知道')))
#判断当前页面title是否包含预期字符串
print(wait.until(EC.title_contains('百度一下，你就知道')))
#能否定位到当前元素
wait.until(EC.presence_of_all_elements_located((By.ID,'kw')))
#判断某个元素是否可见
wait.until(EC.element_to_be_clickable((By.ID,'kw')))




