import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('p1.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user(
                id integer primary key,
                fullname varchar,
                age integer,
                address varchar,
                photo varchar)""")

    def insert_data(self, fullname, age, address, photo):
        self.cursor.execute("INSERT INTO user(fullname, age, address, photo) VALUES (?, ?, ?, ?)",
                            (fullname, age, address, photo))
        self.connection.commit()

    def all_data(self):
        users = self.cursor.execute("SELECT * FROM user")
        return users.fetchall()

    # def one_data(self, id):
    #     fridge = self.cursor.execute("SELECT * FROM fridge WHERE id = ?", (id,))
    #     return fridge.fetchone()
    #
    # def delete_data(self, id):
    #     self.cursor.execute("DELETE FROM fridge WHERE id = ?", (id,))
    #     self.connection.commit()
    #
    # # def update_data(self, id, model, price, year, country):
    # #     self.cursor.execute("UPDATE fridge set model = ?, price = ?, year = ?, country = ? WHERE id = ?",
    # #                         (model, price, year, country, id))
    # #     self.connection.commit()
    #
    # def update_data_model(self, id, model):
    #     self.cursor.execute("UPDATE fridge set model = ? WHERE id = ?",
    #                         (model, id))
    #     self.connection.commit()
    #
    # def update_data_price(self, id, price):
    #     self.cursor.execute("UPDATE fridge set price = ? WHERE id = ?",
    #                         (price, id))
    #     self.connection.commit()
    #
    # def update_data_year(self, id, year):
    #     self.cursor.execute("UPDATE fridge set year = ? WHERE id = ?",
    #                         (year, id))
    #     self.connection.commit()
    #
    # def update_data_country(self, id, country):
    #     self.cursor.execute("UPDATE fridge set country = ? WHERE id = ?",
    #                         (country, id))
    #     self.connection.commit()


