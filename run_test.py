#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-05 11:15
# software: PyCharm

import time
import unittest
from utils.HTMLTestReportCN import HTMLTestRunner
from test_cases.common_test import *
# from utx import *


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(CommonApiTest("test_historyday"))

    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CommonApiTest))
    file_name = f"testResults/test{time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))}.html"
    with open(file_name, 'wb') as result:
        runner = HTMLTestRunner(stream=result,
                                title="测试报告",
                                description="用例执行情况",
                                verbosity=2)
        runner.run(suite)
