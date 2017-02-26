#coding = utf-8
from selenium import webdriver

brower = webdriver.Chrome()

first_url = "http://localhost:8000"

brower.get(first_url)
assert 'Django' in brower.title