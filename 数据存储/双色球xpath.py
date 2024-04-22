from requests_html import HTMLSession
from lxml import etree
url  ='https://datachart.500.com/ssq/history/history.shtml'

session = HTMLSession()
response = session.get(url=url)

print(response.html)
exit(-1)

# print(response.content.decode('gb2312'))

tree = etree.HTML(response.content.decode('gb2312'))
# tree.xpath('//tbody[@id="tdata"]//tr[1]/td[2:8]/text()')

first_tr = tree.xpath('//tbody[@id="tdata"]//tr[1]')[0]
print(type(first_tr))
td_elements = first_tr.xpath('./td[position() >= 2 and position() <= 8]/text()')
total = first_tr.xpath('./td[position()=10]/text()')
big_prize = first_tr.xpath('./td[12]/text()')
print(td_elements)
print(total)
print(big_prize)

# datas = []
# for tr in tree.xpath('//tbody[@id="tdata"]//tr'):
#     td_elements = tr.xpath('./td[position() >= 2 and position() <= 8]/text()')
#     total = tr.xpath('./td[position()=10]/text()')
#     big_prize = tr.xpath('./td[12]/text()')
#     # datas.append((f"号码:{td_elements}, 总奖金{total}, 一等奖{big_prize}"))
#     datas.append((td_elements,total,big_prize))
#     # datas.extend((td_elements,total,big_prize))
# print(datas[0])
