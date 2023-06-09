
import pymysql

def main():
    ...


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

    return(rewards)



if __name__ == "__main__":
    main()