from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
  """百度搜索测试"""
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    self.base_url = "http://www.baidu.com"

  def test_baidu(self):
    """搜索关键字：unittest"""
    driver = self.driver
    driver.get(self.base_url + "/")
    text_input = driver.find_element_by_id("kw")
    btn = driver.find_element_by_id("su")
    text_input.clear()
    text_input.send_keys("unittest")
    btn.click()
    time.sleep(3)
    title = driver.title
    self.assertEqual(title, "unittest_百度搜索")

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main()
