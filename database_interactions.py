import sqlite3


class DatabaseInteractions:
    """
    Utilizes sqlite3 to manipulate databases
    """
    def __init__(self, db):
        self.db = db
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

    def create_table(self, table, params):
        command = "CREATE TABLE {}".format(table)
        command = self.add_list_to_string(command, params)
        try:
            self.cursor.execute(command)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print("***ERROR***: {}\nTable Not Created: {}".format(e, table))

    def insert_row(self, table, data):
        command = "INSERT INTO {} VALUES".format(table)
        command = self.add_list_to_string(command, data)
        try:
            self.cursor.execute(command)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print("***ERROR***: {}\nRow Not Added: {}".format(e, data))

    def insert_multiple(self, table, data):
        command = "INSERT INTO {} Values(".format(table)
        for i in range(len(data[0])):
            command += "?, "
        command = command[:-2] + ")"
        try:
            self.cursor.executemany(command, data)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print("***ERROR***: {}\nRows Not Added: {}".format(e, data))

    def select_column(self, table, column):
        command = "SELECT {} FROM {}".format(column, table)
        try:
            self.cursor.execute(command, {"column": column, "table": table})
            return self.cursor.fetchall()
        except sqlite3.OperationalError as e:
            print("***ERROR*** {}\nColumn Not Selected: {}".format(e, column))

    def select_multiple(self, table, columnlist, orderedby, descending=False):
        command = "SELECT "
        for i in columnlist:
            command += "{}, ".format(i)
        command = command[:-2]
        command += " FROM {} ORDER BY {}".format(table, orderedby)
        if descending:
            command += " DESC"
        print(command)
        try:
            self.cursor.execute(command)
            return self.cursor.fetchall()
        except sqlite3.OperationalError as e:
            print("***ERROR*** {}\nData Not Selected: {}".format(e, columnlist))

    @staticmethod
    def add_list_to_string(string, items):
        string += "("
        for i in items:
            if type(i) == str:
                string += "'{}', ".format(i)
            else:
                string += "{}, ".format(i)
        return string[:-2] + ")"


def test():
    t = "cereals"
    db = "test.db"
    d = DatabaseInteractions(db)
    # d.create_table(t, ('name', 'calories', 'protein'))
    # d.insert_row(t, ("Cereal A", 90, 4))
    col = d.select_column(t, "calories")
    print("COLUMN: ", col)
    cereals = [("Cereal B", 100, 5),
               ("Cereal C", 150, 10)]
    # d.insert_multiple(t, cereals)
    data = d.select_multiple(t, ["calories", "protein"], "calories")
    print("Calories and Protein, sorted by calories:\n", data)
    data = d.select_multiple(t, ["name", "calories", "protein"], "calories", descending=True)
    print("All data, sorted by calories, descending = True:\n", data)


if __name__ == "__main__":
    test()
