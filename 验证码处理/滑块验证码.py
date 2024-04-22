from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains
import re
from requests_html import HTMLSession
from io import BytesIO
from PIL import Image
def get_img(driver,div_class):
    '''
    获取图片坐标以及返回素材图
    :param driver:  q驱动
    :param div_class:  每一个图片所在的class_name
    :return: img, img_list
    '''
    background = driver.find_elements(By.XPATH, div_class)

    # Find all image elements within the parent element
     #查找52个图片元素
    img_url = None
    img_list = []  #存储裁剪的坐标
    print("Number of elements found:", len(background))
    for img in background:
        img_info ={}
        #print(img.get_attribute('style'))
        info = re.findall('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;',img.get_attribute('style'))[0]
        img_url,img_info['x'],img_info['y'] = info
        #转型
        img_info['x'] = int(img_info['x'])
        img_info['y'] = int(img_info['y'])
        img_list.append(img_info)

    #抓取素材图
    session = HTMLSession()
    response = session.get(url=img_url).content
    img_data = BytesIO(response)
    real_image = Image.open(img_data)
    #real_image.show()

    #返回图片以及坐标点
    return real_image,img_list


def get_merge_image(img,img_list):
    '''
    把图片进行裁剪，拼接
    :param img:  要处理的素材图
    :param img_list: 所有的图片定位信息
    :return: 拼接完整的图片
    '''
    img_list_upper = []
    img_list_down = []

    for img_info in img_list:
        if img_info['y'] == -58:
            img_list_upper.append(img.crop((
                                   abs(img_info['x']),
                                   abs(img_info['y']),
                                   abs(img_info['x'])+10,
                                   abs(img_info['y'])+ 58)))
        else:
            img_list_down.append(img.crop((
                                   abs(img_info['x']),
                                   abs(img_info['y']),
                                   abs(img_info['x'])+10,
                                   abs(img_info['y'])+58)))
    #创建空白画布
    new_image = Image.new('RGB',(260,116))
    x_offset = 0
    for i in range(len(img_list_upper)):
        new_image.paste(img_list_upper[i],(x_offset,0))
        new_image.paste(img_list_down[i],(x_offset,58))
        x_offset +=10
    #new_image.show()
    return new_image

def is_similar(complete_img,gap_img,x,y):
    """
    比对每一个像素，从而找到两张图的区别的左上角坐标
    :param complete_img: 完整图片
    :param gap_img: 缺口图片
    :param x: x坐标
    :param y: y坐标
    :return:
    """
    #获取指定坐标的像素点，得到RGB值
    complete_pixel = complete_img.getpixel((x,y))
    gap_pixel = gap_img.getpixel((x,y))
    for i in range(0,3): #遍历3个通道
        #判断两个像素点颜色是否一样
        if abs(complete_pixel[i]-gap_pixel[i]) >50:
            return False
        else:
            return True

def get_diff_location(complete_img,gap_img):
    """
    返回x坐标值
    :param complete_img:
    :param gap_img:
    :return:
    """
    for x in range(1,259):
        for y in range(1,115):
            if not is_similar(complete_img,gap_img,x,y):
                return x



if __name__ == '__main__':

    browser = webdriver.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                 "source": """
                 Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                 })
                 """
             })
    browser.implicitly_wait(10)
    browser.set_window_size(800,800)
    browser.get('http://www.cnbaowen.net/api/geetest')


    #等待滑块加载完成 gt_slider_knob gt_show
    wait = WebDriverWait(browser,10)
    knob = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME,'gt_slider_knob')))
    print(knob)
    browser.implicitly_wait(10)  # 隐性等待，最长等30秒

    #找到完整图片的坐标
    full = get_img(browser,'//*[@id="captcha"]/div/div[1]/div[2]/div[1]/a[2]/div[1]//div')
    #找到缺口图片的坐标
    miss = get_img(browser,'//*[@id="captcha"]/div/div[1]/div[2]/div[1]/a[1]/div[1]//div')

    #得到完整图片
    complete = get_merge_image(*full)
    #得到缺口图片
    gap = get_merge_image(*miss)

    #找到缺口左上角的坐标
    x_ray = get_diff_location(complete,gap)
    print(x_ray)

    action_chain = ActionChains(browser)
    action_chain.click_and_hold(knob)
    action_chain.pause(0.2)
    action_chain.move_by_offset(x_ray -10,0)  #快到缺口了，停顿一下
    action_chain.pause(0.2)
    action_chain.move_by_offset(10,0)
    action_chain.pause(0.5)
    action_chain.release().perform()

    while True:
        pass
