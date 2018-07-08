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
        self.cursor.execute("select name,tel,agroup,flag from %s;" % tableName)
        return  self.cursor.fetchall()

    def getColvalue(self, listName = "agroup", tableName = "mainpreview"):
        self.cursor.execute("select distinct %s from %s;" % (listName, tableName))
        return self.cursor.fetchall()

    def findInTable(self, findStr = '', tableName = "mainpreview"):
        self.cursor.execute("select name,tel,agroup from %s where name like '%%%s%%' or tel like '%%%s%%' or agroup like '%%%s%%';" % (tableName,findStr,findStr,findStr))
        return self.cursor.fetchall()

    def dataWriteToSql(self, Data, tableName = "mainpreview"):
        print("add:",Data)
        self.cursor.execute("insert into %s values('%s','%s','%s','%s','%s','%s','%s','%s');"
                            % (tableName,
                               Data['name'],
                               Data['tel'],
                               Data['agroup'],
                               Data['flag'],
                               Data['email'],
                               Data['address'],
                               Data['remark'],
                               Data['birthday']))
        self.db.commit()

    def dataUpdateToSql(self, Data, tableName = "mainpreview"):
        print("update:",Data)
        self.cursor.execute("update %s set ;"
                            % (tableName,
                               Data['name'],
                               Data['tel'],
                               Data['agroup'],
                               Data['flag'],
                               Data['email'],
                               Data['address'],
                               Data['remark'],
                               Data['birthday']))
        self.db.commit()

    def delDataFromDB(self,Data = [], tableName = "mainpreview"):
        print("delete:",Data)
        self.cursor.execute("delete from %s where tel = '%s';" % (tableName, Data))
        self.db.commit()

    def getDataFromDB(self,Data =[], tableName = "mainpreview"):
        self.cursor.execute("select * from %s where  tel = '%s';" % (tableName, Data))
        return self.cursor.fetchone()