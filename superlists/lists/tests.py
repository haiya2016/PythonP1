from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')    #resolve 用于从根路径“/“查找函数
		self.assertEqual(found.func, home_page)

		
