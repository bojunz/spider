from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import undetected_chromedriver as uc
from lxml import etree

option = webdriver.ChromeOptions()
s_url = 'https://sellercentral.amazon.com/reportcentral/api/v1/getOnlineReportRecords?type=CustomerReturns&size=50&offset=0&sDate=&eDate=&days=365&sDateOff=0&eDateOff=0&cols=returned_date&cols=return_reason&cols=msku&cols=fnsku&cols=lpn&cols=merchant_fulfillment_order_id&cols=title&cols=disposition&cols=fc_id&cols=asin&cols=returned_quantity&cols=customer_comment&cols=status&filter={"filterKey":"lpn","value":"LPNRRGM8080511","operation":"Equals"}&&sort={"keyName":"returned_date","sortingOrder":"DESC"}'
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
cookies = 'ubid-main=133-0998889-2534942; i18n-prefs=USD; session-id-apay=135-9678718-9944321; skin=noskin; s_nr=1702889397304-New; s_vnum=2134889397305%26vn%3D1; s_dslv=1702889397305; s_sq=%5B%5BB%5D%5D; ld=NSGoogle; ubid-acbus=134-7536941-1904252; s_pers=%20s_fid%3D650CBB86BFFB0676-1D2FE3A80DA47429%7C1861079067100%3B%20s_dl%3D1%7C1703228067101%3B%20gpv_page%3DUS%253ASD%253ASOA-home%7C1703228067102%3B%20s_ev15%3D%255B%255B%2527NSGoogle%2527%252C%25271703226267103%2527%255D%255D%7C1861079067103%3B; s_sess=%20s_cc%3Dtrue%3B%20s_ppvl%3DUS%25253ASD%25253ASOA-home%252C8%252C8%252C703%252C1536%252C703%252C1536%252C864%252C1.25%252CL%3B%20c_m%3Dwww.google.comNatural%2520Search%3B%20s_sq%3D%3B%20s_ppv%3DUS%25253ASD%25253ASOA-home%252C8%252C8%252C703%252C1536%252C703%252C1536%252C864%252C1.25%252CL%3B; session-id=145-2010954-5303703; lc-main=en_US; aws-session-id=700-6538274-7601094; aws-analysis-id=700-6538274-7601094; _mkto_trk=id:112-TZM-766&token:_mch-amazon.com-1703473533225-84392; aws-session-id-time=1703473533l; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19717%7CMCMID%7C35490442893049014664208017722446535784%7CMCAAMLH-1704078334%7C9%7CMCAAMB-1704078334%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1703480734s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; regStatus=pre-register; s_cc=true; csm-hit=tb:QZ9JJ6SN3PWKRYAQVX1M+s-EZT8WGFB0JQ0Q8J5MYYB|1703552932727&t:1703552932727&adb:adblk_no; session-id-time=2334272949l; session-token="WziJpnS0ov1tVhE4OlCIulmjISYX6lSr2HB1r5DOOi5VFG0DfX0ArPiPCCZ/PBP0W4EIObRiBBa8dZ8GO8XJZDshedSfhBJjucReslA18O9WPTmW6Hkfwxek68DdG8p35ZTwgh7CS7TASNVKe/bIpUwkvCe1Xelh/Qi97E2d0Y5oB5x8S4xRAWA6RDDcuiTV18cixolxqPPKMU9ph7+TmfcHDhQTTtUcH6P4sqcIkG03nWueruQsx539QNhyGCgZs3K317lvRO5YefjW7eWGX7VbfMkHjYYrB7epNWgSvf/dpfEzXAoxxIA2rW02C9xySIeonSzXK2EzksP3eD3aRmy0p3DH4tglzYUYII5C7wSkMbHPoi4FJw=="; x-main="psRbqO1EeZWuMDJq9MCtTiCSby2?IILui9d4fN9S8nYYMM8rdK1GrPG2OhhQ6Z6g"'
#option.add_argument('USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"')
option.add_argument('user-agent=' + ua)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")

#browser = uc.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe",options=option)
browser = uc.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
             "source": """
             Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
             })
             """
         })
browser.implicitly_wait(10)
browser.set_window_size(800,800)

judege = os.path.exists('cookies.json')

def login_process():
    # browser.get(r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0')
    browser.get(s_url)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, 'ap_email'))
    )
    browser.find_element(By.ID, 'ap_email').send_keys('bojunz@timetecinc.com')
    browser.find_element(By.ID, 'ap_password').send_keys('zbj1999$')
    browser.find_element(By.ID, 'signInSubmit').click()
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="picker-container"]/div/div[2]/div/div/div/div[2]/button/div/div'))
    )
    browser.find_element(By.XPATH, '//*[@id="picker-container"]/div/div[2]/div/div/div/div[2]/button/div/div').click()
    time.sleep(1)
    browser.find_element(By.XPATH,
                         '//*[@id="picker-container"]/div/div[2]/div/div[3]/div/div[3]/button/div/div').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="picker-container"]/div/div[3]/div/button').click()

def save_cookie():
    with open("cookies.json", "w") as f:
        json.dump(browser.get_cookies(), f)


#cookie函数
def create_cookie():
    if not judege:
        print('no cookie')
        login_process()
        save_cookie()
    else:
        print('with cookie')
        #cookie_login()

#browser.find_element(By.XPATH, '//*[@id="katal-id-87"]').send_keys('LPNtest')
#browser.find_element(By.XPATH, '//*[@id="online-report-btn"]//button').click()
login_process()
browser.implicitly_wait(10)
html = browser.page_source #获取当前页面源数据
print(browser.page_source)
tree = etree.HTML(html)
print(tree)
while True:
    pass