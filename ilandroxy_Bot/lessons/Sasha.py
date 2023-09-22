# region Домашка: ************************************************************



# endregion Домашка: ************************************************************


# region Урок: ************************************************************

import sqlite3 as sq


db = sq.connect("sqlite.db")
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            user_id INTEGER,
                            username TEXT,
                            name TEXT)
                """)
db.commit()
cur.execute("INSERT INTO users VALUES(?, ?, ?)", (1232142, 'ilandroxxy', 'Ilya'))
db.commit()

# endregion db_start()


# endregion Урок: ************************************************************



# todo: Александра = []
# на прошлом уроке: Обсудили сложную домашку по машинному обучению, надо читать материалы
# на следующем уроке:
