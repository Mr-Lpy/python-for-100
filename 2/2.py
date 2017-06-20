# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import pymysql
import random
import string

def generate_code(count, length):
    forSelect = string.ascii_letters + string.digits
    arr = []
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        yield Re

class MakeCodes:
    def __init__(self):
        self.codes = []

    def connectDB(self):
        try:
            self.conn = pymysql.connect(host='localhost',user='root',password='123456',db='test',port=3306,charset='utf8')
            self.cur = self.conn.cursor()
            return True
        except Exception as e:
            print("connect err:" + e)
            return False        

    def closeDB(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print('close error:' + e)

    def makeCodes(self):
        self.codes = generate_code(200,20)

    def insertCodes(self):
        try:
            sql = 'INSERT INTO codes(code) VALUES (%s);'
            for code in self.codes:
                print(code)
                print(self.cur.execute(sql,(code)))
            self.conn.commit()
        except Exception as e:
            print('insert error:' + e) 

    def getCodes(self):
        try:
            sql = 'select * from codes;'
            self.cur.execute(sql)
            codes = self.cur.fetchall()

            for code in codes:
                print("ID: " + str(code[0]) + '    name: ' + code[1])
        except Exception as e:
            print('getcode error:' + e) 

if __name__ == '__main__' :
    handler = MakeCodes()
    if handler.connectDB() == False:
        print('connect failed')
    else:
        print('connect successed')
        handler.makeCodes()
        handler.insertCodes()
        handler.getCodes()
        handler.closeDB()
    
