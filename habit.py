import pymysql
import pandas as pd
import Reward from rewards

def main():

    print(get_acumulated_rewards())


def connect_to_database():

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='JoAnJuCa13',
        database='habits'
    )

    return conn

def get_habits():
    
    conn = connect_to_database()

    cursor = conn.cursor()
    sql = 'SELECT * FROM habit'
    cursor.execute(sql)
    habits = cursor.fetchall()

    return habits

def add_to_historial(id):
    
    conn = connect_to_database()

    cursor = conn.cursor()
    sql = 'CALL add_habit_to_historial(%s);'
    cursor.execute(sql, (id))
    conn.commit()
    conn.close

def get_acumulated_rewards():

    conn = connect_to_database()

    cursor = conn.cursor()
    sql = 'CALL get_acumulated_rewards;'
    cursor.execute(sql)
    rewards = cursor.fetchall()

    column_names = [column[0] for column in cursor.description]
    rw = pd.DataFrame(rewards, columns=column_names)
    rw.set_index('id', inplace=True)

    return(rw)

def add_reward(reward_id):

    conn = connect_to_database()

    cursor = conn.cursor()
    sql = 'CALL add_reward(%s);'
    cursor.execute(sql, (reward_id))
    conn.commit()
    conn.close

if __name__ == "__main__":
    main()