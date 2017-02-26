#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

brower = webdriver.Chrome()

first_url = "https://www.oschina.net/home/login"

brower.get(first_url)
print("web: %s" %(first_url))
print("------ begin login -------")
title = brower.title
print("title is : %s" %(title))

brower.find_element_by_id("userMail").send_keys("18565557140")
brower.find_element_by_id("userPassword").send_keys("250214445wjx")
brower.find_element_by_class_name("btn-login").click()
time.sleep(3)
print("------ after login -------")
title = brower.title
print("title is : %s" %(title))
url = brower.current_url
print("当前页面的网址是：%s" %(url))

info = brower.find_element_by_class_name("name").text
print("当前登录的用户是：%s"  %(info)) 

cookie = brower.get_cookies()
for co in cookie:
	print("%r -> %r" %(co['name'], co['value']))

brower.set_window_size(600, 600)

js = "window.scrollTo(600 , 600);"
brower.execute_script(js)



