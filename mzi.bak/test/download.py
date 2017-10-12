import sqlite3
import requests
from bs4 import BeautifulSoup
import os
import random
import time

class download():
    def __init__(self):
        # self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"]

        # self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"} 
        
        # self.headers = {
        #     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #     "Accept-Encoding":"gzip, deflate",
        #     "Accept-Language":"zh-CN,zh;q=0.8",
        #     "Cache-Control":"max-age=0",
        #     "Host":"www.mzitu.com",            
        #     "Proxy-Connection":"keep-alive",
        #     "Upgrade-Insecure-Requests":"1",
        #     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        #     "If-Modified-Since":"Sat, 05 Aug 2017 :11:59 GMT"

        # }
        # self.headers = {                
        #         "Host": "www.mzitu.com",
        #         "Proxy-Connection": "keep-alive",
        #         "Upgrade-Insecure-Requests": "1",
        #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #         "Referer": "http://www.mzitu.com/1/3",
        #         "Accept-Encoding": "gzip, deflate",
        #         "Accept-Language": "zh-CN,zh;q=0.8",
        #         "Cookie": "Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1501686261,1501842451,1501849821,1501919031; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1501932178"

        #     }

        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
                    
                    "Referer": "http://www.mzitu.com/1/3",

                }




               
        self.picpath = 'images'
        if not os.path.exists(self.picpath):
            os.makedirs(self.picpath)
    


    def getconn(self):
        self.conn = sqlite3.connect('mzi.db')
        self.cur = self.conn.cursor()

    def closeconn(self):
        self.cur.close()
        self.conn.close()

    def create_folder(self):
        self.getconn()
        sql = 'select hpath from allurl'
        self.cur.execute(sql)
        pathname_lis = self.cur.fetchall()
        for pathname in pathname_lis:
            # print pathname[0]
            deta_path =os.path.join(self.picpath,pathname[0])
            # print deta_path
            os.makedirs(deta_path)
        self.closeconn()

    def downimg(self):        
        os.chdir(self.picpath)
        for i in range(1,66):   
            # IP = '180.175.249.189:9000'

            # proxy = {'http': IP}

            first_url = 'http://www.mzitu.com/103681/' + str(i)

            img_html = requests.get(first_url,headers=self.headers,timeout =6)
            # img_html = requests.get(first_url,headers=self.headers,proxies=proxy,timeout =6)

            img_Soup = BeautifulSoup(img_html.text,'html.parser')
            img_url = img_Soup.find('div',class_='main-image').find('img')['src']

            
            img = requests.get(img_url,headers=self.headers)

            f = open(str(i) + '.jpg','ab')
            f.write(img.content)
            f.close()  


            print first_url + ' success download!'

        

down = download()
# down.create_folder()
down.downimg()


