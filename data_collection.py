from scraping import Requests, DataExtractor
from database_interactions import DatabaseInteractions

DATABASE = "world_currencies.db"
API_REQ_LIMIT = 100


class Collector:
    """
    A class to organize the collection of data and send it to the database
    """
    def __init__(self):
        self.req = Requests()
        self.data = {}
        self.dates = {}
        self.req_counter = self.check_req_counter()

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

    def collect_data(self):
        if len(self.dates) + self.req_counter >= API_REQ_LIMIT:
            print("ERROR: Request Count Too High \n\tCurrent = " + str(self.req_counter) + "\n\tRequested = " + str(
                len(self.dates)))
            return
        for date in self.dates:
            self.store_data(self.req.historical_data(date))

    def store_data(self, data):
        pass


def test_client():
    c = Collector()
    print(c.check_req_counter())
    c.req_counter = 40
    c.update_req_counter()
    print(c.check_req_counter())


if __name__ == "__main__":
    test_client()
