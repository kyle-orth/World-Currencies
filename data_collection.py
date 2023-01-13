
from scraping import Requests, DataExtractor
from database_interactions import DatabaseInteractions

API_REQ_LIMIT = 100


class Collector:
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
            print("ERROR: Request Count Too High \n\tCurrent = " + str(self.req_counter) + "\n\tRequested = " + str(len(self.dates)))
            return
        for date in self.dates:
            data = self.req.historical_data(date)
            self.store_data(DataExtractor(data))

    def store_data(self, extractor):
        date = extractor.date()
        data = extractor.exchange_rates()


def test_client():
    Collector.zero_req_counter()
    print(Collector.check_req_counter())

    c = Collector()
    c.req_counter = 40
    c.update_req_counter()
    print(Collector.check_req_counter())


if __name__ == "__main__":
    test_client()
