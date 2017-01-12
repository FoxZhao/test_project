import unittest, time
from HTMLTestRunner import HTMLTestRunner

test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':

  now = time.strftime("%Y%m%d%H%M%S")
  report_name = "./report/" + now + "_test_report.html"
  fp = open(report_name, 'wb')
  runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况：")
  runner.run(discover)
  fp.close()