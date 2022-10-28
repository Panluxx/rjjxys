# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:52
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : run.py
# Software  : PyCharm

import pytest
import os
import subprocess
from Common.config import p_path

xml_report_path = os.path.join(p_path.root_path, 'Report', 'xml')
detail_report_path = os.path.join(p_path.root_path, 'Report', 'detail_report')


def batch(CMD):
    output, errors = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    outs = output.decode("utf-8")
    return outs


if __name__ == '__main__':
    # 冒烟测试命令
    """pytest.main(["-m", "smoke", "-s", "-v", "--reruns", "2", "--reruns-delay", "5",
                  "--html=Outputs/reports/pytest_report.html", "--alluredir=Outputs/allure/history"])
    """
    # 重运行机制  立马重运行  "--reruns","1", "--reruns-delay", "5" 失败后5s内重运行一次
    """["-s", "-v", "--reruns", "1", "--reruns-delay", "5", "--html=Outputs/reports/pytest_reports.html",
                      "--alluredir=Outputs/allure/history"]
    """
    # pytest.main(["-vs", "./TestCases/test_login.py"])

    args = ["--alluredir", xml_report_path]
    test_result = pytest.main(args)
    cmd = "allure generate {0} -o {1} --clean".format(xml_report_path, detail_report_path)
    reportResult = batch(cmd)


