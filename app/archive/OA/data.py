import pymysql
import pandas as pd

class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='JoAnJuCa13',
            database='oi'
        )

    def get_task(self):
        cursor = self.conn.cursor()
        sql = 'CALL get_task;'
        cursor.execute(sql)
        tasks = cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(tasks, columns=column_names)
        return(df)
    
    def add_task(self, task):
        cursor = self.conn.cursor()
        sql = 'CALL add_task(%s);'
        cursor.execute(sql, task)
        self.conn.commit()
        print('TASK ADDED')

    def delete_first_task(self):
        cursor = self.conn.cursor()
        sql = 'CALL delete_first_task;'
        cursor.execute(sql)
        self.conn.commit()
        print('FIRST TASK DELETED')


DataBase = DB()