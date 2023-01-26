from data_collection import Collector
from database_interactions import DatabaseInteractions

DATABASE = "world_currency_history.db"
TABLE = "exchange_rates"
CSV_FILE = "world_currency_history.csv"


def add_dates(dates):
    collect = Collector(DATABASE, TABLE)
    # collect.create_table()
    collect.collect_data(dates)


def get_table():
    db = DatabaseInteractions(DATABASE)
    print(db.select_multiple(TABLE, ["date", "USD", "JPY", "EUR"], "date", descending=True))
    db.end()


def delete_rows(dates):
    db = DatabaseInteractions(DATABASE)
    for date in dates:
        criteria = "date ='{}'".format(date)
        db.delete_row(TABLE, criteria, 'date', offset=1)
    db.end()


def convert_to_csv(p=False):
    db = DatabaseInteractions(DATABASE)
    db.convert_to_csv(TABLE, CSV_FILE, p=p)
    db.end()


if __name__ == "__main__":
    newDay = False
    requestData = True
    deleteData = False
    getData = False
    csv = True

    dates_list = []
    for i in range(12):
        month = str(i + 1)
        if len(month) == 1:
            month = "0{}".format(month)
        dates_list.append("2022-{}-26".format(month))  # SETUP FOR NEXT TIME!

    if newDay:
        Collector.zero_req_counter()

    if requestData:
        add_dates(dates_list)

    if deleteData:
        delete_rows(dates_list)

    if getData:
        get_table()

    if csv:
        convert_to_csv(p=True)
