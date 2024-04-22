from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import undetected_chromedriver as uc
from lxml import etree


def login_process():
    browser.get(r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0')

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


def cookie_login():
    with open("../LPN爬虫/cookies.json", "r", encoding="utf-8") as f:
        listCookies = json.load(f)
        for cookie in listCookies:
            # print(cookie)
            cookie_dict = {
                 "domain": cookie.get("domain"),
                 "name": cookie.get("name"),
                 "value": cookie.get("value"),
                 "expiry": cookie.get("expiry"),
                 "path": cookie.get("path"),
                 "httpOnly": False,
                 "sameSite": "Lax",
                 "secure": False,
            }
            print("Before adding cookies:", browser.get_cookies())
            browser.add_cookie(cookie_dict)
            print("After adding cookies:", browser.get_cookies())
        browser.refresh()
        browser.get(r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0')


def cookie_login2():
    with open("../LPN爬虫/cookies.json", "r", encoding="utf-8") as f:
        listCookies = json.load(f)
        # Clear existing cookies
        browser.delete_all_cookies()
        for cookie in listCookies:
            cookie_dict = {
                 "domain": cookie.get("domain"),
                 "name": cookie.get("name"),
                 "value": cookie.get("value"),
                 # "expiry": cookie.get("expiry"),
                 "path": cookie.get("path"),
                 "httpOnly": False,
                 "sameSite": "Lax",
                 "secure": False,
            }
            browser.add_cookie(cookie_dict)
            print(cookie_dict)
        time.sleep(3)
        browser.refresh()
        print('new cookie')
        browser.get(r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0')


def cookie_login3():
    browser.delete_all_cookies()
    cookie_dict = {"domain": "sellercentral.amazon.com", "expiry": 1733775915, "httpOnly": False, "name": "csm-hit", "path": "/", "sameSite": "Lax", "secure": False, "value": "tb:s-NST94JMAGAMSF7SSR9T1|1703535915359&t:1703535915403&adb:adblk_no"}
    browser.add_cookie(cookie_dict)

    time.sleep(3)
    browser.refresh()
    browser.get(r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0')

def login_process():
    browser.get(r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0')

    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, 'ap_email'))
    )
    browser.find_element(By.ID, 'ap_email').send_keys('bojunz@timetecinc.com')
    browser.find_element(By.ID, 'ap_password').send_keys('zbj1999$')
    browser.find_element(By.ID, 'signInSubmit').click()
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="picker-container"]/div/div[2]/div/div/div/div[2]/button/div/div'))
    )
    browser.find_element(By.XPATH, '//*[@id="picker-container"]/div/div[2]/div/div/div/div[2]/button/div/div').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="picker-container"]/div/div[2]/div/div[3]/div/div[3]/button/div/div').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="picker-container"]/div/div[3]/div/button').click()