#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-05 11:45
# software: PyCharm

import unittest
import requests
from config.apis import *


class CommonApiTest(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        pass

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_historyday(self):
        url = host_common + history_day_api
        params = {"type": 0}
        res = requests.get(url, params=params, headers=header)
        self.assertEqual(200, res.status_code)
