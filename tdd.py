#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.brower = webdriver.Chrome()
		self.brower.implicitly_wait(10)

	def tearDown(self):
		self.brower.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.brower.get('http://localhost:8000')

		self.assertIn('To-Do', self.brower.title)
		header_text = self.brower.find_element_by_tag_name('h1').text
		self.fail("Finish the test")

		#应用可以输入一个待办事项
		inputbox = self.brower.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		#文本框中输入了“buy a car"
		inputbox.send_keys('buy a car')

		#按下回车键，返回显示"1：buy a car"
		inputbox.send_keys(keys.ENTER)

		table = self.brower.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: buy a car' for row in rows)
			)

if __name__ == '__main__':
	unittest.main()


