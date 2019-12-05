#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-05 11:15
# software: PyCharm

import time
import unittest
from utils.HTMLTestReportCN import HTMLTestRunner
from test_cases.common_test import *
from utx import *

# 手动下载安装utx https://github.com/jianbing/utx


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

    # setting.run_case = {Tag.ALL}
    # setting.check_case_doc = False
    # setting.full_case_name = True
    # setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
    # setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
    # setting.sort_case = True  # 是否按照编写顺序，对用例进行排序
    # setting.create_report_by_style_1 = False  # 测试报告样式1
    # setting.create_report_by_style_2 = True  # 测试报告样式2
    # setting.show_print_in_console = True
    #
    # runner = TestRunner()
    # runner.add_case_dir(r'test_cases')
    # runner.run_test()
