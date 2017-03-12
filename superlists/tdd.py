#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.brower = webdriver.Chrome()
		self.brower.implicitly_wait(10)

	def tearDown(self):
		self.brower.quit()

	def check_for_rows_in_list_table(self, row_text):
		table = self.brower.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.brower.get('http://localhost:8000')

		self.assertIn('To-Do', self.brower.title)
		header_text = self.brower.find_element_by_tag_name('h1').text
		

		#应用可以输入一个待办事项
		inputbox = self.brower.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)
		#文本框中输入了“buy a car"
		inputbox.send_keys('buy a car')
		#按下回车键，返回显示"1：buy a car"
		inputbox.send_keys(Keys.ENTER)
		# time.sleep(10)

		inputbox = self.brower.find_element_by_id('id_new_item')
		inputbox.send_keys('buy a computer')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_rows_in_list_table('1: buy a car')
		self.check_for_rows_in_list_table('2: buy a caomputer')
		self.fail("Finish the test")

if __name__ == '__main__':
	unittest.main()


