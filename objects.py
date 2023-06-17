import pymysql
import pandas as pd



class Reward:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='JoAnJuCa13',
            database='habits'
        )

    def get_acumulated(self):
        cursor = self.conn.cursor()
        sql = 'CALL get_acumulated_rewards;'
        cursor.execute(sql)
        rewards = cursor.fetchall()

        column_names = [column[0] for column in cursor.description]
        rw = pd.DataFrame(rewards, columns=column_names)
        rw.set_index(rw.columns[0], inplace=True)

        return(rw)

reward = Reward()
