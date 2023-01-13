from data_collection import Collector
from database_interactions import DatabaseInteractions


def add_dates(dates):
    collect = Collector("world_currency_history.db", "exchange_rates")
    collect.create_table()
    collect.collect_data(dates)


def get_table():
    db = DatabaseInteractions("world_currency_history.db")
    print(db.select_multiple("exchange_rates", ["date", "USD", "JPY", "EUR"], "USD", descending=False))


if __name__ == "__main__":
    dates_list = []
    for i in range(12):
        month = str(i + 1)
        if len(month) == 1:
            month = "0{}".format(month)
        dates_list.append("2014-{}-01".format(month))

    requestData = False
    if requestData:
        add_dates(dates_list)

    getData = True
    if getData:
        get_table()
