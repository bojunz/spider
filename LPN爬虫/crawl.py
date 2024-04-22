import requests

headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
cookie = 'ubid-main=133-0998889-2534942; i18n-prefs=USD; session-id-apay=135-9678718-9944321; skin=noskin; s_nr=1702889397304-New; s_vnum=2134889397305%26vn%3D1; s_dslv=1702889397305; s_sq=%5B%5BB%5D%5D; ld=NSGoogle; ubid-acbus=134-7536941-1904252; s_pers=%20s_fid%3D650CBB86BFFB0676-1D2FE3A80DA47429%7C1861079067100%3B%20s_dl%3D1%7C1703228067101%3B%20gpv_page%3DUS%253ASD%253ASOA-home%7C1703228067102%3B%20s_ev15%3D%255B%255B%2527NSGoogle%2527%252C%25271703226267103%2527%255D%255D%7C1861079067103%3B; s_sess=%20s_cc%3Dtrue%3B%20s_ppvl%3DUS%25253ASD%25253ASOA-home%252C8%252C8%252C703%252C1536%252C703%252C1536%252C864%252C1.25%252CL%3B%20c_m%3Dwww.google.comNatural%2520Search%3B%20s_sq%3D%3B%20s_ppv%3DUS%25253ASD%25253ASOA-home%252C8%252C8%252C703%252C1536%252C703%252C1536%252C864%252C1.25%252CL%3B; session-id=145-2010954-5303703; lc-main=en_US; csm-hit=tb:8B3CKPJX5GN428GXF8BB+s-YG6BG84F6RH7H0PWBTEQ|1703226283604&t:1703226283604&adb:adblk_no; session-id-time=2333946285l; x-main="NeGlEfGuCsAMVp40CbCIUvc3TlguRmzz?XlC36?iuktfdgr9jALZvGf9xfzNsAuL"; session-token=EMpk+lT4DFNAIJu+qUQyXPpWOTzNwxg8LFjZiM+kcgHkw7LWsh/PPyx5VRl5QLMiAkb4xAV6eW4q1vm5FOiiA8Gf0kpANONgwD7h+SigYy7NBBuqaJ8PTTorTFdHKVbC2RMDY8/1HzuzChvmLI0IQq6Au958zymt5jXb5dAaWS8KaBt+cCI+Fq72pplWDqCTx9OEsjQk8/+xpcyVKST8jBSxe5TiLSln3Ey9jXQjZ+ZP35hM4hKZ5Ko+MHVs6E624WNefFyhDsWETAlMau/i0eN4KgIC4LrDryUt6IqRamJre4b//7X60Bb5SffiSSlHNz6ZXS6oCiEDBcrEWFG+EizO/9pCu3nTVi0wHu+2Aa02IjrNWZdJpJQrveRnVzaE'
cookie_dict ={}
for i in cookie.split('; '):
    cookie_dict[i.split('=')[0]] = i.split('=')[1]
# url = 'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0/%7B%22filters%22:[%22%22,%22%22,%22%22,%22%22,%22LPNRRGN2360984%22],%22pageOffset%22:1,%22searchDays%22:180%7D'
url = r'https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/0'
response = requests.get(url=url,headers=headers,cookies=cookie_dict)
response.encoding='utf-8'
print(response.text)
print(response.status_code)