from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


chrome_path = 'D:\\software\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
url = 'https://www.baidu.com'
driver.get(url)

# 输入内容
driver.find_element_by_id('kw').send_keys(u'大熊猫')

driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot('daxiongmao.png')

driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys(u'航空母舰')

driver.find_element_by_id('su').send_keys(Keys.RETURN)

driver.find_element_by_id('kw').clear()

print(driver.get_cookies())
driver.close()
