#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import unittest

from prayertimes.prayertimes import PrayTimes


class TestPT(unittest.TestCase):

    CITY_LAT = 48.66
    CITY_LNG = 2.33
    CITY_UTC = +1
    DATE = datetime.date.today()

    def setUp(self):
        self.pt = PrayTimes("ISNA")
        self._t = self.pt.get_times(date=self.DATE, coords=(self.CITY_LAT, self.CITY_LNG), utc_offset=self.CITY_UTC)

    def test_instance_test(self):
        self.assertTrue(isinstance(self.pt, PrayTimes))
        self.assertTrue(isinstance(self._t, dict))
        self.test_instance_pt()

    def test_instance_pt(self):
        for i in ['fajr', 'sunrise', 'dhuhr', 'asr', 'maghrib', 'isha']:
            self.assertTrue(isinstance(self._t[i], str))

    def test_running(self):
        self.pt.set_method("Makkah")
        self.pt.adjust({"asr": "Hanafi"})
        self._t = self.pt.get_times(date=self.DATE, coords=(self.CITY_LAT, self.CITY_LNG), utc_offset=self.CITY_UTC)

        self.test_instance_pt()

        self.pt.tune({'fajr': +10, 'dhuhr': -10, 'asr': -10, 'maghrib': -10, 'isha': +10,
                      'midnight': 5, 'sunrise': -2, 'sunset': +9, 'imsak': +15})

        self._t = self.pt.get_times(date=self.DATE, coords=(self.CITY_LAT, self.CITY_LNG), utc_offset=self.CITY_UTC)

        self.test_instance_pt()


if __name__ == '__main__':
    unittest.main()
