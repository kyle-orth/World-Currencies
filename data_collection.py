from scraping import Requests, DataExtractor
from database_interactions import DatabaseInteractions

DATABASE = "world_currencies.db"
API_REQ_LIMIT = 100
CURRENCY_KEYS = ["USD", "EUR", "JPY", "CAD", "HKD", "KRW", "AUD", "RUB", "NZD", "GBP", "INR", "CHF"]


class Collector:
    """
    A class to organize the collection of data and send it to the database
    """
    def __init__(self, database, table_name):
        self.req = Requests()
        self.req_counter = self.check_req_counter()
        self.db = DatabaseInteractions(database)
        self.table = table_name

    @staticmethod
    def check_req_counter():
        try:
            with open('request_counter.pickle', 'r') as file:
                val = file.read()
                if val != '':
                    return int(val)
        except FileNotFoundError:
            pass
        return 0

    @staticmethod
    def zero_req_counter():
        with open('request_counter.pickle', 'w') as file:
            file.write('0')

    def update_req_counter(self):
        with open('request_counter.pickle', 'w') as file:
            file.write(str(self.req_counter))

    def collect_data(self, dates):
        if len(dates) + self.req_counter > API_REQ_LIMIT:
            print("ERROR: Request Count Too High \n\tCurrent = " + str(self.req_counter) + "\n\tRequested = " + str(
                len(dates)))
            return
        for date in dates:
            self.store_data(DataExtractor(self.req.historical_data(date)))
            self.req_counter += 1
            self.update_req_counter()
        print("New request counter: {} / {}".format(self.req_counter, API_REQ_LIMIT))

    def store_data(self, extractor):
        exchange_rates = extractor.exchange_rates()
        data = [extractor.date]
        for key in CURRENCY_KEYS:
            data.append(exchange_rates[key])
        self.db.insert_row(self.table, data)

    def create_table(self):
        dataHeaders = ["date"]
        for i in range(len(CURRENCY_KEYS)):
            dataHeaders.append(CURRENCY_KEYS[i])
        self.db.create_table(self.table, dataHeaders)


def test_client():
    c = Collector("test.db", "test")
    print(c.check_req_counter())
    c.req_counter = 40
    c.update_req_counter()
    print(c.check_req_counter())


if __name__ == "__main__":
    test_client()
