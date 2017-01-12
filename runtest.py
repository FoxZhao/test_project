import unittest, time, os, smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

# 定义发送邮件
def send_email(newest_report):
  # 获取最新的测试报告内容
  f = open(newest_report, 'rb')
  mail_body = f.read()
  f.close

  sender = "zhaozihaozz@126.com"
  password = "52gsbyzzh"
  receiver = "395381480@qq.com"
  # 定义邮件内容
  mail = MIMEText(mail_body, 'html', 'utf-8')
  mail['Subject'] = Header(u"自动化测试报告", 'utf-8')
  mail['From'] = sender
  mail['To'] = receiver
  #发送邮件
  smtp = smtplib.SMTP()
  smtp.connect('smtp.126.com')
  smtp.login(sender, password)
  smtp.sendmail(sender, receiver, mail.as_string())
  smtp.quit()
  print("email has send out!")

# 定义获取最新报告的方法，report_dir为报告文件夹的路径
def get_newest_report(report_dir):
  #获取所有report文件的数组
  lists = os.listdir(report_dir)
  #根据最后修正时间倒序排序，最新的报告为数组第一个文件
  lists.sort(key=lambda fn: os.path.getmtime(report_dir + fn), reverse=True)
  #拼接最新报告的路径
  newest_report = os.path.join(report_dir, lists[0])
  return newest_report

if __name__ == '__main__':

  report_dir = "./report/"
  test_dir = "./test_case"
  #找到所有的测试用例
  discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

  now = time.strftime("%Y%m%d%H%M%S")
  report_name = report_dir + now + "_test_report.html"
  fp = open(report_name, 'wb')
  #执行测试用例并生成测试报告
  runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况：")
  runner.run(discover)
  fp.close()

  newest_report = get_newest_report(report_dir)
  send_email(newest_report)
