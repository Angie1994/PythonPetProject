import sys
import pymysql

class sqlOperate(object):
    def openSQL(self):
        # 尝试连接到数据库，如果不成功则打印失败信息
        try:
            self.db = pymysql.connect("localhost", "tj", "", "addresslistdata", charset="utf8")
            self.cursor = self.db.cursor()
            self.cursor.execute("select count(*) from mainpreview")
            count = self.cursor.fetchone()
        except:
            QMessageBox.critical(self, "警告", "无法打开数据！")
            quit()

        self.dataRow = int(count[0])

    def readAllSQL(self, tableName = "mainpreview"):
        self.cursor.execute("select * from %s;" % tableName)
        data = self.cursor.fetchall()
        return data

    def getColvalue(self, listName = "agroup", tableName = "mainpreview"):
        self.cursor.execute("select distinct %s from %s;" % (listName, tableName))
        data = self.cursor.fetchall()
        return data

    def findInTable(self, findStr = '', tableName = "mainpreview"):
        self.cursor.execute("select * from %s where name like '%%%s%%' or tel like '%%%s%%' or agroup like '%%%s%%';" % (tableName,findStr,findStr,findStr))
        data = self.cursor.fetchall()
        print(data)
        return data
