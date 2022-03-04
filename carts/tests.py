from django.test import TestCase

# Create your tests here.

from django.contrib import auth
from .models import *

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = Userprofile.objects.create_user('test@dom.com', 'iamtest', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', pas