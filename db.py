import pymysql
from base import rabbit_prod_DATABASES, rabbit_test_DATABASES


class Crud:
    def __init__(self):
        alidb_config = rabbit_prod_DATABASES
        self.conn = pymysql.connect(
            host=alidb_config["HOST"],
            port=alidb_config["PORT"],
            user=alidb_config["USER"],
            password=alidb_config["PASSWORD"],
            db=alidb_config["DB"],
            charset=alidb_config["CHARSET"],
        )
        self.cursor = self.conn.cursor()

    def crud(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            return e

    def select(self, sql):
        num = self.cursor.execute(sql)
        self.conn.commit()
        return num

    def __del__(self):
        self.cursor.close()
        self.conn.close()

def db_insert(problem, answer):
    sql = 'insert into content(problem, answer) values("{}", "{}")'.format(problem, answer)
    Crud().crud(sql)
