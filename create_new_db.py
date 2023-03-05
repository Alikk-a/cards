import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"dictionary_my.db"
    # описание столбцов словаря - id номер, слово и значение
    sql_create_dictionary_table = """ CREATE TABLE IF NOT EXISTS dictionary_full (
                                        id integer PRIMARY KEY,
                                        word1 text,
                                        meaning1 text,
                                        trans1 text,
                                        dop1 text,
                                        type1 text,
                                        meandop1 text,
                                        meantype1 text,
                                        word2 text,
                                        meaning2 text,
                                        trans2 text,
                                        dop2 text,
                                        type2 text,
                                        meandop2 text,
                                        meantype2 text,
                                        word3 text,
                                        meaning3 text,
                                        trans3 text,
                                        dop3 text,
                                        type3 integer,
                                        meandop3 text,
                                        meantype3 text,
                                        dataen text,
                                        winen integer,
                                        imgen text,
                                        texten text,
                                        dataru text,
                                        winru integer,
                                        imgru text,
                                        textru text
                                    ); """


    # подключение к базе
    conn = create_connection(database)

    # создание таблицы dictionary
    if conn is not None:
        create_table(conn, sql_create_dictionary_table)
    else:
        print("Ошибка: не удалось подключиться к базе.")


if __name__ == '__main__':
    main()