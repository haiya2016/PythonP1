from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')    #resolve 用于从根路径“/“查找函数
		self.assertEqual(found.func, home_page)

	def test_home_page_retruns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))  #断言响应的content属性以html标签开头
		self.assertIn(b'<title>To-Do list<title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))		
