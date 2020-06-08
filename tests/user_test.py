import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='njahirakaranja',password='12345')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)