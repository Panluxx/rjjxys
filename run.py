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
import shutil

xml_report_path = os.path.join(p_path.root_path, 'Report', 'xml')
detail_report_path = os.path.join(p_path.root_path, 'Report', 'detail_report')
screenshots_path = os.path.join(p_path.root_path, 'Report', 'screenshots')


def batch(CMD):
    """
    执行 shell 命令并返回输出

    Returns:
        (stdout, stderr, returncode) 元组
    """
    result = subprocess.run(
        CMD,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8',
        errors='replace'
    )
    return result.stdout, result.stderr, result.returncode


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

    # 清理截图目录（安全删除，目录不存在不报错）
    if os.path.exists(screenshots_path):
        shutil.rmtree(screenshots_path)
    os.makedirs(screenshots_path, exist_ok=True)

    args = ["--alluredir", xml_report_path]
    pytest.main(args)

    cmd = "allure generate {0} -o {1} --clean".format(xml_report_path, detail_report_path)
    stdout, stderr, returncode = batch(cmd)

    if returncode != 0:
        print(f"Allure 报告生成失败 (返回码: {returncode})")
        if stderr:
            print(f"错误信息: {stderr}")
    else:
        print(f"Allure 报告生成成功: {detail_report_path}")
