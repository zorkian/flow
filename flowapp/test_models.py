import unittest

from django.test import TestCase

from .models import Account, AccountStatus, AccountType


class AccountTests(TestCase):
    def setUp(self):
        self.robot = Account(name='robot', accounttype=AccountType.ROLE)
        self.mark = Account(name='mark')
        self.toad = Account(name='toad', accountstatus=AccountStatus.DISABLED)

    def test_is_role(self):
        self.assertTrue(self.robot.is_role_account)
        self.assertFalse(self.mark.is_role_account)

    def test_is_user(self):
        self.assertTrue(self.mark.is_user)
        self.assertFalse(self.robot.is_user)

    def test_is_enabled(self):
        self.assertTrue(self.mark.is_enabled)
        self.assertFalse(self.toad.is_enabled)

    def test_is_disabled(self):
        self.assertTrue(self.toad.is_disabled)
        self.assertFalse(self.mark.is_disabled)
