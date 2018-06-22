from django.test import TestCase
from Billsplitter.forms import generateUserList
from django.contrib.auth.models import User

class UserListTestCase(TestCase):
	def setUp(self):
		u_l = User.objects.create("first_name" = "Test", id = -1)
		
	def test_generate_user_list(self):
		self.AssertEqual(generateUserList(u_l), [(-1, "Test")])