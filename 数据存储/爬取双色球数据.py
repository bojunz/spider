from requests_html import HTMLSession
import pymysql
from pymongo import MongoClient
from lxml import etree

class Spider:
    def __init__(self):
        self.url  ='https://datachart.500.com/ssq/history/history.shtml'
        self.session = HTMLSession()

    def parse(self):
        datas = []
        response = self.session.get(url=self.url)
        tree = etree.HTML(response.content.decode('gb2312'))
        for tr in tree.xpath('//tbody[@id="tdata"]//tr'):
            sql_data = []
            td_elements = tr.xpath('./td[position() >= 2 and position() <= 8]/text()')
            total = tr.xpath('./td[position()=10]/text()')
            big_prize = tr.xpath('./td[12]/text()')
            # sql_data.append((td_elements,total,big_prize,))
            sql_data = [str(td_elements),str(total),str(big_prize)]
            datas.append((f"号码:{td_elements}, 总奖金{total}, 一等奖{big_prize}"))
            self.SaveMysql(sql_data)

    def Connect(self):
        host = 'localhost'
        port = 3306
        db = 'spider'
        user = 'admin'
        password = 'qwe123'

        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
        self.cursor = self.conn.cursor()

    def SaveMysql(self,data):

        # 插入数据
        self.cursor.execute(f"""insert into ssq(S_number,total_prize,bigPrize) values("{data[0]}","{data[1]}","{data[2]}");""")
        self.conn.commit()


    def run(self):
        self.parse()
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    spider = Spider()
    spider.Connect()
    spider.run()