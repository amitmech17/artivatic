from utilities.test_status import Status
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time
import requests
import json
from datetime import datetime


class ApiTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def test_t1Api(self):
        self.log.info("test_t1Api started")
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
            data = requests.get(
                'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22',
                headers=headers)
            data_json = data.json()
            dates = []
            list = data_json['list']
            for li in list:
                temp = li['main']['temp']
                temp_min = li['main']['temp_min']
                temp_max = li['main']['temp_max']
                if temp < temp_min and temp > temp_max:
                    self.log.info("Temperature is not within min and max limit")
                    assert True == False
                date_time = datetime.strptime(li['dt_txt'], "%Y-%m-%d %H:%M:%S")
                if len(dates) > 0:
                    delta = date_time - dates[-1]
                    if delta.seconds != 3600:
                        self.log.info("Some Hours are missing")
                        assert True == False
                        break
                if li['weather'][0]['id'] == 500:
                    if li['weather'][0]['description'] != "light rain":
                        self.log.info("weather description is not according to id = 500")
                        assert True == False

                if li['weather'][0]['id'] == 800:
                    if li['weather'][0]['description'] != "clear sky":
                        self.log.info("weather description is according to id = 800")
                        assert True == False
                dates.append(date_time)
            first_date = dates[0]
            last_date = dates[-1]
            date_delta = last_date.date() - first_date.date()
            self.log.info("Temperature is within min and max limit")
            self.log.info("All the Hours are present")
            self.log.info("weather description is according to id 800 and 500")
            if date_delta.days != 4:
                print("data of 4 days is not present")
                assert True == False
            self.log.info("data of 4 days is present")
        except Exception as e:
            self.log.info("Error in Api call" + e)


