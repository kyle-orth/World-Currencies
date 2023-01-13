import requests


API_KEY = "?api_key=" + "71c4f1decacf4799d756de5e374e257cbeca25db"
CURRENCY_KEYS = ["USD", "EUR", "JPY", "CAD", "HKD", "KRW", "AUD", "RUB", "NZD", "GBP", "INR", "CHF"]


class Requests:
    """
    A class to scrape data from a world currency exchange website.
    May be useful to create a base site for webscraping for future use.
    """
    def __init__(self):
        self.baseURL = "https://api.getgeoapi.com/v2/currency/"
        self.api_key = "?api_key=" + "71c4f1decacf4799d756de5e374e257cbeca25db"
        self.statusCode = 0

    def request(self, endpoint):
        return requests.get(self.baseURL + endpoint + self.api_key)

    def currency_list(self):
        currencies = self.request("list")
        self.statusCode = currencies.status_code
        return currencies.json()

    def historical_data(self, date):
        data = self.request("historical/" + date)
        self.statusCode = data.status_code
        return data.json()


class DataExtractor:
    """
    Interprets the data that the Requests class pulls from the website
    """
    def __init__(self, historical_rates):
        print(historical_rates)
        self.date = historical_rates["updated_date"]
        self.rates = historical_rates["rates"]

    def names(self):
        n = {}
        for country in CURRENCY_KEYS:
            n[country] = self.rates[country]["currency_name"]
        return n

    def exchange_rates(self):
        r = {}
        for country in CURRENCY_KEYS:
            r[country] = self.rates[country]["rate"]
        return r


class Examples:
    """Showcases the potential uses of Requests and DataExtractor. First example uses sample data
    for extraction. The second example pulls the data of a given date using the Requests class,
    then interprets that data with the DataExtractor."""
    @staticmethod
    def example():
        sampleRates = {'base_currency_code': 'EUR', 'base_currency_name': 'Euro', 'amount': '1.0000', 'updated_date': '2023-01-10', 'rates': {'ZAR': {'currency_name': 'South African rand', 'rate': '18.3118', 'rate_for_amount': '18.3118'}, 'SAR': {'currency_name': 'Saudi riyal', 'rate': '4.0323', 'rate_for_amount': '4.0323'}, 'CNY': {'currency_name': 'Renminbi', 'rate': '7.2903', 'rate_for_amount': '7.2903'}, 'XAF': {'currency_name': 'Central African CFA franc', 'rate': '656.7957', 'rate_for_amount': '656.7957'}, 'JPY': {'currency_name': 'Japanese yen', 'rate': '142.1183', 'rate_for_amount': '142.1183'}, 'CHF': {'currency_name': 'Swiss franc', 'rate': '0.9892', 'rate_for_amount': '0.9892'}, 'EUR': {'currency_name': 'Euro', 'rate': '1.0000', 'rate_for_amount': '1.0000'}, 'GBP': {'currency_name': 'Pound sterling', 'rate': '0.8817', 'rate_for_amount': '0.8817'}, 'USD': {'currency_name': 'United States dollar', 'rate': '1.0753', 'rate_for_amount': '1.0753'}, 'NGN': {'currency_name': 'Nigerian naira', 'rate': '483.3978', 'rate_for_amount': '483.3978'}, 'DKK': {'currency_name': 'Danish krone', 'rate': '7.4516', 'rate_for_amount': '7.4516'}, 'SGD': {'currency_name': 'Singapore dollar', 'rate': '1.4301', 'rate_for_amount': '1.4301'}, 'HKD': {'currency_name': 'Hong Kong dollar', 'rate': '8.3978', 'rate_for_amount': '8.3978'}, 'INR': {'currency_name': 'Indian rupee', 'rate': '87.7419', 'rate_for_amount': '87.7419'}, 'NOK': {'currency_name': 'Norwegian krone', 'rate': '10.7419', 'rate_for_amount': '10.7419'}, 'SEK': {'currency_name': 'Swedish krona', 'rate': '11.1935', 'rate_for_amount': '11.1935'}, 'CAD': {'currency_name': 'Canadian dollar', 'rate': '1.4409', 'rate_for_amount': '1.4409'}, 'AED': {'currency_name': 'United Arab Emirates dirham', 'rate': '3.9462', 'rate_for_amount': '3.9462'}, 'BIF': {'currency_name': 'Burundian franc', 'rate': '2202.9140', 'rate_for_amount': '2202.9140'}, 'RWF': {'currency_name': 'Rwandan franc', 'rate': '1142.5699', 'rate_for_amount': '1142.5699'}, 'TZS': {'currency_name': 'Tanzanian shilling', 'rate': '2504.3011', 'rate_for_amount': '2504.3011'}, 'UGX': {'currency_name': 'Ugandan shilling', 'rate': '3980.9677', 'rate_for_amount': '3980.9677'}, 'KES': {'currency_name': 'Kenyan shilling', 'rate': '132.8817', 'rate_for_amount': '132.8817'}, 'AUD': {'currency_name': 'Australian dollar', 'rate': '1.5591', 'rate_for_amount': '1.5591'}, 'GYD': {'currency_name': 'Guyanese dollar', 'rate': '224.0860', 'rate_for_amount': '224.0860'}, 'MVR': {'currency_name': 'Maldivian rufiyaa', 'rate': '16.7419', 'rate_for_amount': '16.7419'}, 'MRU': {'currency_name': 'Mauritanian ouguiya', 'rate': '38.9355', 'rate_for_amount': '38.9355'}, 'KWD': {'currency_name': 'Kuwaiti dinar', 'rate': '0.3333', 'rate_for_amount': '0.3333'}, 'STN': {'currency_name': 'São Tomé and Príncipe dobra', 'rate': '24.5161', 'rate_for_amount': '24.5161'}, 'NAD': {'currency_name': 'Namibian dollar', 'rate': '18.3011', 'rate_for_amount': '18.3011'}, 'HTG': {'currency_name': 'Haitian gourde', 'rate': '158.0430', 'rate_for_amount': '158.0430'}, 'GNF': {'currency_name': 'Guinean franc', 'rate': '9189.2473', 'rate_for_amount': '9189.2473'}, 'FJD': {'currency_name': 'Fijian dollar', 'rate': '2.3763', 'rate_for_amount': '2.3763'}, 'MOP': {'currency_name': 'Macanese pataca', 'rate': '8.6452', 'rate_for_amount': '8.6452'}, 'XCD': {'currency_name': 'Eastern Caribbean dollar', 'rate': '2.9032', 'rate_for_amount': '2.9032'}, 'SLL': {'currency_name': 'Sierra Leonean leone', 'rate': '20408.2796', 'rate_for_amount': '20408.2796'}, 'SYP': {'currency_name': 'Syrian pound', 'rate': '2700.0000', 'rate_for_amount': '2700.0000'}, 'FKP': {'currency_name': 'Falkland Islands pound', 'rate': '0.8817', 'rate_for_amount': '0.8817'}, 'SHP': {'currency_name': 'Saint Helena pound', 'rate': '0.8817', 'rate_for_amount': '0.8817'}, 'BWP': {'currency_name': 'Botswana pula', 'rate': '13.6774', 'rate_for_amount': '13.6774'}, 'SOS': {'currency_name': 'Somali shilling', 'rate': '607.5269', 'rate_for_amount': '607.5269'}, 'MGA': {'currency_name': 'Malagasy ariary', 'rate': '4822.5806', 'rate_for_amount': '4822.5806'}, 'VUV': {'currency_name': 'Vanuatu vatu', 'rate': '123.8280', 'rate_for_amount': '123.8280'}, 'GIP': {'currency_name': 'Gibraltar pound', 'rate': '0.8817', 'rate_for_amount': '0.8817'}, 'LSL': {'currency_name': 'Lesotho loti', 'rate': '18.1828', 'rate_for_amount': '18.1828'}, 'CUP': {'currency_name': 'Cuban peso', 'rate': '25.8065', 'rate_for_amount': '25.8065'}, 'ALL': {'currency_name': 'Albanian lek', 'rate': '117.5054', 'rate_for_amount': '117.5054'}, 'BSD': {'currency_name': 'Bahamian dollar', 'rate': '1.0753', 'rate_for_amount': '1.0753'}, 'BZD': {'currency_name': 'Belize dollar', 'rate': '2.1505', 'rate_for_amount': '2.1505'}, 'MWK': {'currency_name': 'Malawian kwacha', 'rate': '1093.0645', 'rate_for_amount': '1093.0645'}, 'AFN': {'currency_name': 'Afghan afghani', 'rate': '96.4839', 'rate_for_amount': '96.4839'}, 'MNT': {'currency_name': 'Mongolian tögrög', 'rate': '3715.8280', 'rate_for_amount': '3715.8280'}, 'SVC': {'currency_name': 'Salvadoran colón', 'rate': '9.4086', 'rate_for_amount': '9.4086'}, 'QAR': {'currency_name': 'Qatari riyal', 'rate': '3.9140', 'rate_for_amount': '3.9140'}, 'DJF': {'currency_name': 'Djiboutian franc', 'rate': '190.8602', 'rate_for_amount': '190.8602'}, 'AWG': {'currency_name': 'Aruban florin', 'rate': '1.9140', 'rate_for_amount': '1.9140'}, 'ERN': {'currency_name': 'Eritrean nakfa', 'rate': '16.2043', 'rate_for_amount': '16.2043'}, 'VND': {'currency_name': 'Vietnamese đồng', 'rate': '25208.6022', 'rate_for_amount': '25208.6022'}, 'PEN': {'currency_name': 'Peruvian sol', 'rate': '4.0860', 'rate_for_amount': '4.0860'}, 'PHP': {'currency_name': 'Philippine peso', 'rate': '58.9032', 'rate_for_amount': '58.9032'}, 'HUF': {'currency_name': 'Hungarian forint', 'rate': '399.0215', 'rate_for_amount': '399.0215'}, 'MXN': {'currency_name': 'Mexican peso', 'rate': '20.5699', 'rate_for_amount': '20.5699'}, 'MZN': {'currency_name': 'Mozambican metical', 'rate': '67.9785', 'rate_for_amount': '67.9785'}, 'TTD': {'currency_name': 'Trinidad and Tobago dollar', 'rate': '7.2581', 'rate_for_amount': '7.2581'}, 'COP': {'currency_name': 'Colombian peso', 'rate': '5162.7097', 'rate_for_amount': '5162.7097'}, 'CLP': {'currency_name': 'Chilean peso', 'rate': '890.5806', 'rate_for_amount': '890.5806'}, 'EGP': {'currency_name': 'Egyptian pound', 'rate': '29.7312', 'rate_for_amount': '29.7312'}, 'RON': {'currency_name': 'Romanian leu', 'rate': '4.9462', 'rate_for_amount': '4.9462'}, 'BYN': {'currency_name': 'Belarusian ruble', 'rate': '2.7097', 'rate_for_amount': '2.7097'}, 'NZD': {'currency_name': 'New Zealand dollar', 'rate': '1.6882', 'rate_for_amount': '1.6882'}, 'BGN': {'currency_name': 'Bulgarian lev', 'rate': '1.9570', 'rate_for_amount': '1.9570'}, 'BHD': {'currency_name': 'Bahraini dinar', 'rate': '0.4086', 'rate_for_amount': '0.4086'}, 'BMD': {'currency_name': 'Bermudian dollar', 'rate': '1.0753', 'rate_for_amount': '1.0753'}, 'LBP': {'currency_name': 'Lebanese pound', 'rate': '1618.8172', 'rate_for_amount': '1618.8172'}, 'ANG': {'currency_name': 'Netherlands Antillean guilder', 'rate': '1.9140', 'rate_for_amount': '1.9140'}, 'OMR': {'currency_name': 'Omani rial', 'rate': '0.4086', 'rate_for_amount': '0.4086'}, 'MKD': {'currency_name': 'Macedonian denar', 'rate': '61.5914', 'rate_for_amount': '61.5914'}, 'YER': {'currency_name': 'Yemeni rial', 'rate': '268.7957', 'rate_for_amount': '268.7957'}, 'TJS': {'currency_name': 'Tajikistani somoni', 'rate': '10.9892', 'rate_for_amount': '10.9892'}, 'GMD': {'currency_name': 'Gambian dalasi', 'rate': '65.3763', 'rate_for_amount': '65.3763'}, 'SBD': {'currency_name': 'Solomon Islands dollar', 'rate': '8.9140', 'rate_for_amount': '8.9140'}, 'SRD': {'currency_name': 'Surinamese dollar', 'rate': '34.0538', 'rate_for_amount': '34.0538'}, 'PYG': {'currency_name': 'Paraguayan guaraní', 'rate': '7914.8280', 'rate_for_amount': '7914.8280'}, 'ISK': {'currency_name': 'Icelandic króna', 'rate': '154.8065', 'rate_for_amount': '154.8065'}, 'JOD': {'currency_name': 'Jordanian dinar', 'rate': '0.7634', 'rate_for_amount': '0.7634'}, 'PGK': {'currency_name': 'Papua New Guinean kina', 'rate': '3.7849', 'rate_for_amount': '3.7849'}, 'ZMW': {'currency_name': 'Zambian kwacha', 'rate': '19.6774', 'rate_for_amount': '19.6774'}, 'PAB': {'currency_name': 'Panamanian balboa', 'rate': '1.0753', 'rate_for_amount': '1.0753'}, 'KHR': {'currency_name': 'Cambodian riel', 'rate': '4416.1290', 'rate_for_amount': '4416.1290'}, 'SZL': {'currency_name': 'Swazi lilangeni', 'rate': '18.3118', 'rate_for_amount': '18.3118'}, 'CVE': {'currency_name': 'Cape Verdean escudo', 'rate': '110.2688', 'rate_for_amount': '110.2688'}, 'PLN': {'currency_name': 'Polish złoty', 'rate': '4.6989', 'rate_for_amount': '4.6989'}, 'RSD': {'currency_name': 'Serbian dinar', 'rate': '117.1290', 'rate_for_amount': '117.1290'}, 'BBD': {'currency_name': 'Barbadian dollar', 'rate': '2.1505', 'rate_for_amount': '2.1505'}, 'KRW': {'currency_name': 'South Korean won', 'rate': '1338.3118', 'rate_for_amount': '1338.3118'}, 'BRL': {'currency_name': 'Brazilian real', 'rate': '5.6129', 'rate_for_amount': '5.6129'}, 'VES': {'currency_name': 'Venezuelan bolívar', 'rate': '19.9677', 'rate_for_amount': '19.9677'}, 'UAH': {'currency_name': 'Ukrainian hryvnia', 'rate': '39.3226', 'rate_for_amount': '39.3226'}, 'IQD': {'currency_name': 'Iraqi dinar', 'rate': '1568.2796', 'rate_for_amount': '1568.2796'}, 'DZD': {'currency_name': 'Algerian dinar', 'rate': '146.4946', 'rate_for_amount': '146.4946'}, 'BND': {'currency_name': 'Brunei dollar', 'rate': '1.4301', 'rate_for_amount': '1.4301'}, 'CDF': {'currency_name': 'Congolese franc', 'rate': '2146.1720', 'rate_for_amount': '2146.1720'}, 'GTQ': {'currency_name': 'Guatemalan quetzal', 'rate': '8.4301', 'rate_for_amount': '8.4301'}, 'TRY': {'currency_name': 'Turkish lira', 'rate': '20.1828', 'rate_for_amount': '20.1828'}, 'TWD': {'currency_name': 'New Taiwan dollar', 'rate': '32.7097', 'rate_for_amount': '32.7097'}, 'XDR': {'currency_name': 'Special drawing rights', 'rate': '0.8065', 'rate_for_amount': '0.8065'}, 'GHS': {'currency_name': 'Ghanaian cedi', 'rate': '10.7312', 'rate_for_amount': '10.7312'}, 'XPF': {'currency_name': 'CFP franc', 'rate': '119.1398', 'rate_for_amount': '119.1398'}, 'LKR': {'currency_name': 'Sri Lankan rupee', 'rate': '392.9462', 'rate_for_amount': '392.9462'}, 'UZS': {'currency_name': 'Uzbekistani soʻm', 'rate': '12150.8387', 'rate_for_amount': '12150.8387'}, 'TND': {'currency_name': 'Tunisian dinar', 'rate': '3.3226', 'rate_for_amount': '3.3226'}, 'XOF': {'currency_name': 'West African CFA franc', 'rate': '656.7957', 'rate_for_amount': '656.7957'}, 'BAM': {'currency_name': 'Bosnia and Herzegovina convertible mark', 'rate': '1.9677', 'rate_for_amount': '1.9677'}, 'LAK': {'currency_name': 'Lao kip', 'rate': '18266.6667', 'rate_for_amount': '18266.6667'}, 'AZN': {'currency_name': 'Azerbaijani manat', 'rate': '1.8280', 'rate_for_amount': '1.8280'}, 'ETB': {'currency_name': 'Ethiopian birr', 'rate': '57.4839', 'rate_for_amount': '57.4839'}, 'BDT': {'currency_name': 'Bangladeshi taka', 'rate': '111.5054', 'rate_for_amount': '111.5054'}, 'THB': {'currency_name': 'Thai baht', 'rate': '35.9570', 'rate_for_amount': '35.9570'}, 'GEL': {'currency_name': 'Georgian lari', 'rate': '2.8925', 'rate_for_amount': '2.8925'}, 'CZK': {'currency_name': 'Czech koruna', 'rate': '24.0000', 'rate_for_amount': '24.0000'}, 'TMT': {'currency_name': 'Turkmenistan manat', 'rate': '3.6022', 'rate_for_amount': '3.6022'}, 'UYU': {'currency_name': 'Uruguayan peso', 'rate': '42.8172', 'rate_for_amount': '42.8172'}, 'AMD': {'currency_name': 'Armenian dram', 'rate': '424.3333', 'rate_for_amount': '424.3333'}, 'MMK': {'currency_name': 'Burmese kyat', 'rate': '2251.1828', 'rate_for_amount': '2251.1828'}, 'HNL': {'currency_name': 'Honduran lempira', 'rate': '26.4086', 'rate_for_amount': '26.4086'}, 'NPR': {'currency_name': 'Nepalese rupee', 'rate': '140.7097', 'rate_for_amount': '140.7097'}, 'MAD': {'currency_name': 'Moroccan dirham', 'rate': '10.9892', 'rate_for_amount': '10.9892'}, 'NIO': {'currency_name': 'Nicaraguan córdoba', 'rate': '38.7634', 'rate_for_amount': '38.7634'}, 'MDL': {'currency_name': 'Moldovan leu', 'rate': '20.5054', 'rate_for_amount': '20.5054'}, 'DOP': {'currency_name': 'Dominican peso', 'rate': '60.5806', 'rate_for_amount': '60.5806'}, 'JMD': {'currency_name': 'Jamaican dollar', 'rate': '162.6129', 'rate_for_amount': '162.6129'}, 'ARS': {'currency_name': 'Argentine peso', 'rate': '193.9892', 'rate_for_amount': '193.9892'}, 'PKR': {'currency_name': 'Pakistani rupee', 'rate': '244.9355', 'rate_for_amount': '244.9355'}, 'RUB': {'currency_name': 'Russian ruble', 'rate': '74.7097', 'rate_for_amount': '74.7097'}, 'CRC': {'currency_name': 'Costa Rican colón', 'rate': '626.8817', 'rate_for_amount': '626.8817'}, 'AOA': {'currency_name': 'Angolan kwanza', 'rate': '541.7097', 'rate_for_amount': '541.7097'}, 'BTN': {'currency_name': 'Bhutanese ngultrum', 'rate': '88.5914', 'rate_for_amount': '88.5914'}, 'IRR': {'currency_name': 'Iranian rial', 'rate': '45161.2903', 'rate_for_amount': '45161.2903'}, 'ILS': {'currency_name': 'Israeli new shekel', 'rate': '3.7204', 'rate_for_amount': '3.7204'}, 'KMF': {'currency_name': 'Comorian franc', 'rate': '492.2581', 'rate_for_amount': '492.2581'}, 'BOB': {'currency_name': 'Bolivian boliviano', 'rate': '7.3656', 'rate_for_amount': '7.3656'}, 'LRD': {'currency_name': 'Liberian dollar', 'rate': '165.3871', 'rate_for_amount': '165.3871'}, 'MUR': {'currency_name': 'Mauritian rupee', 'rate': '46.8280', 'rate_for_amount': '46.8280'}, 'IDR': {'currency_name': 'Indonesian rupiah', 'rate': '16758.0645', 'rate_for_amount': '16758.0645'}, 'KGS': {'currency_name': 'Kyrgyzstani som', 'rate': '92.1075', 'rate_for_amount': '92.1075'}, 'TOP': {'currency_name': 'Tongan paʻanga', 'rate': '2.5376', 'rate_for_amount': '2.5376'}, 'SCR': {'currency_name': 'Seychellois rupee', 'rate': '15.0323', 'rate_for_amount': '15.0323'}, 'WST': {'currency_name': 'Samoan tālā', 'rate': '2.8710', 'rate_for_amount': '2.8710'}, 'LYD': {'currency_name': 'Libyan dinar', 'rate': '5.1505', 'rate_for_amount': '5.1505'}, 'KYD': {'currency_name': 'Cayman Islands dollar', 'rate': '0.8817', 'rate_for_amount': '0.8817'}, 'HRK': {'currency_name': 'Croatian kuna', 'rate': '7.5710', 'rate_for_amount': '7.5710'}, 'MYR': {'currency_name': 'Malaysian ringgit', 'rate': '4.6989', 'rate_for_amount': '4.6989'}, 'CUC': {'currency_name': 'Cuban convertible peso', 'rate': '1.0753', 'rate_for_amount': '1.0753'}, 'KZT': {'currency_name': 'Kazakhstani tenge', 'rate': '497.0645', 'rate_for_amount': '497.0645'}, 'SDG': {'currency_name': 'Sudanese pound', 'rate': '607.6882', 'rate_for_amount': '607.6882'}, 'SSP': {'currency_name': 'South Sudanese pound', 'rate': '726.9329', 'rate_for_amount': '726.9329'}, 'ZWL': {'currency_name': 'Zimbabwean dollar', 'rate': '734.5430', 'rate_for_amount': '734.5430'}, 'IMP': {'currency_name': 'Manx pound', 'rate': '0.8857', 'rate_for_amount': '0.8857'}, 'JEP': {'currency_name': 'Jersey pound', 'rate': '0.8857', 'rate_for_amount': '0.8857'}, 'GGP': {'currency_name': 'Guernsey pound', 'rate': '0.8857', 'rate_for_amount': '0.8857'}, 'XAU': {'currency_name': 'Gold (troy ounce)', 'rate': '0.0006', 'rate_for_amount': '0.0006'}, 'XAG': {'currency_name': 'Silver (troy ounce)', 'rate': '0.0460', 'rate_for_amount': '0.0460'}}, 'status': 'success'}
        extractor = DataExtractor(sampleRates)
        print(extractor.date)
        print(extractor.exchange_rates())

    @staticmethod
    def example_request(date):
        requestor = Requests()
        todays_data = requestor.historical_data(date)
        print(requestor.statusCode)
        print(todays_data)

        if requestor.statusCode == 200:
            extractor = DataExtractor(todays_data)
            print(extractor.date)
            print(extractor.names())
            print(extractor.exchange_rates())


if __name__ == "__main__":
    Examples.example_request("2010-10-24")
