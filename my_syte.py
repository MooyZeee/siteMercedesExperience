import sqlite3 as sq

conn = ''


def open():
    global conn
    try:
        conn = sq.connect("user.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS data_user (
                    login TEXT,
                    password TEXT,
                    age INTEGER,
                    lang TEXT
                    )""")
    except Exception as ex:
        print(ex)
    else:
        return cur


def menu():
    print("1-Зарегистрироваться\n2-Войти")
    ans = input("Ваш выбор: ")
    return ans


def prover(ans):
    if ans == '1':
        data = register()
        register_insert(data)
    elif ans == '2':
        login, password = log_in()
        result_log_in = select_data(login, password)
        if result_log_in:
            print("Имя:", result_log_in[0][0])
            print("Ваш пароль:", result_log_in[0][1])
            print("Ваш возраст:", result_log_in[0][3])
        else:
            print("Неправильный логин или пароль!")


def register():
    login = input("Введите логин: ")
    password = input("Введтие пароль: ")
    age = input("Введите возраст: ")
    lang = input("Какие языки программирования вы знаете? ")
    return login, password, age, lang


def register_insert(data):
    cur = open()
    cur.execute("""INSERT INTO data_user (login, password, age, lang) VALUES (?, ?, ?, ?)""", data)
    conn.commit()


def select_data(login, password):
    cur = open()
    cur.execute("SELECT * FROM data_user WHERE login = (?) and password = (?)", (login, password))
    return cur.fetchall()


def log_in():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password


def main():
    ans = menu()
    prover(ans)


main()
