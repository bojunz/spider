from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()

browser.set_window_size(800,800)

browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#按照标签id值查找
browser.switch_to.frame('iframeResult')
#按照下标查找
# browser.switch_to.frame(0)

#定位目标
div = browser.find_element(By.ID,'draggable')
#使用动作链
action = ActionChains(browser)
action.click_and_hold(div) #点击并且坚持住
for i in range(10):
    #移动,第一个参数为x轴，第二个参数为y轴
    action.move_by_offset(28,0).perform() #perform执行
    time.sleep(0.1)
time.sleep(2)
#释放拿起的鼠标
action.release().perform()
time.sleep(5)
