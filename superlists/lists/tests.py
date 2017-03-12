from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')    #resolve 用于从根路径“/“查找函数
		self.assertEqual(found.func, home_page)

	# def test_home_page_retruns_correct_html(self):
	# 	request = HttpRequest()
	# 	response = home_page(request)
	# 	# self.assertTrue(response.content.startswith(b'<html>'))  #断言响应的content属性以html标签开头
	# 	# self.assertIn(b'<title>To-Do lists</title>', response.content)
	# 	# self.assertTrue(response.content.endswith(b'</html>'))
	# 	expected_html = render_to_string('home.html')
	# 	print(expected_html)
	# 	print(response.content.decode())
	# 	print(response.content)

	# 	self.assertEqual(response.content.decode(), expected_html)	

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)
		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'}
			)
		print(expected_html)
		print(response.content.decode())
		self.assertEqual(response.content.decode(), expected_html)

