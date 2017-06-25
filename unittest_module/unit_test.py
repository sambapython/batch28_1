import unittest
from app import c1
class TestsAdd(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "login to system"
		cls.app = c1()
	@classmethod
	def tearDownClass(cls):
		print "teadonw class"
		del cls.app
		print "logout from the system."
	def setUp(self):
		print "pre configuration"

	def tearDown(self):
		print "remove the config belongs to test case."

	def test_1add_10_20(self):
		print "test1"
		exp=30
		act=self.app.add(10,20)
		self.assertEqual(exp,act)

	def test_2add_str1_str2(self):
		print "test2"
		exp="str1str2"
		act=self.app.add("str1","str2")
		self.assertEqual(exp,act)

	def test_3add_str1_20(self):
		print "testy3"
		exp=None
		act=self.app.add("str1",20)
		self.assertEqual(exp,act)


if __name__ == "__main__":
	unittest.main()

