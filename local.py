#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

brower = webdriver.Chrome()
# brower.maximize_window()

file_path = 'file:///' + os.path.abspath('test.html')

brower.get(file_path)

brower.implicitly_wait(10)

print("测试checkbox")
inputs = brower.find_elements_by_tag_name('input')
 

for i in inputs:
	if i.get_attribute('type') == 'checkbox':
		i.click()
		time.sleep(0.5)

brower.find_elements_by_css_selector('input[type=checkbox]').pop().click()


print("测试alter窗口")
brower.find_element_by_name('alterbutton').click()
# time.sleep(1)


brower.switch_to_alert().accept()
# time.sleep(1)


print("测试文件上传")
brower.find_element_by_name('attach[]').send_keys('D:\OneDrive\autotest\local.py')
# time.sleep(1)


print("测试prompt窗口")
brower.find_element_by_name('promptbutton').click()
# time.sleep(1)
s_alert = brower.switch_to_alert()
s_alert.send_keys('hello, world')
# time.sleep(1)
s_alert.accept()
# time.sleep(1)
s_alert.accept()

print("测试confirm窗口")
brower.find_element_by_name('confirmbutton').click()
# time.sleep(1)
s_alert.accept()
# time.sleep(1)
s_alert.accept()


print("测试下拉窗口")
s1 = brower.find_element_by_id('Selector')
s1.find_element_by_xpath("//option[@value='banana']").click()

brower.find_element_by_id('showSelectResult').click()
# time.sleep(1)
s_alert.accept()


print("测试文本框")
brower.find_element_by_id('edit').send_keys('测试文本框')
brower.find_element_by_name('submit').click()
# time.sleep(1)
s_alert.accept()


print("测试radiobox")
ra = brower.find_element_by_id('radio')
ra.find_element_by_xpath("//input[@class='Baidu']").click()

ra1 = ra.find_elements_by_xpath("//label")
for i in ra1:
	print(i.text)
