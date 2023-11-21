import pymysql
"""
导入连接MySQL需要的包，没有安装pymysql需要先安装
使用命令行切换到python的安装路径下的scripts子目录下安装（pip install pymysql）
"""

class MysqlConnector(object):
    def __init__(self, host, port, user, pwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.database = database

    def executeSql(self, sql):
        db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, database=self.database)
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results

if __name__ == '__main__':
    db=MysqlConnector('114.113.116.57', 33039, 'xj_lims', 'xj_hdat3#sd', 'xj_lims')
    print(db.executeSql(' desc gjj_data_up '))
