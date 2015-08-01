from django.db import models
from django_enumfield import enum

class AccountType(enum.Enum):
	ROLE = 0
	USER = 1

class AccountStatus(enum.Enum):
	ENABLED = 0
	DISABLED = 1

class Account(models.Model):
	"""Account is someone that might author content

	This might be a person or a role account or some other account type that we
	don't have today.
	"""
	name = models.CharField(max_length=128)
	email = models.EmailField()
	api_key = models.CharField(max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	accounttype = enum.EnumField(AccountType, default=AccountType.USER)
	accountstatus = enum.EnumField(AccountStatus, default=AccountStatus.ENABLED)

	def is_user(self):
		return self.accounttype == AccountType.USER

	def is_role_account(self):
		return self.accounttype == AccountType.ROLE

	def is_enabled(self):
		return self.accountstatus == AccountStatus.ENABLED

	def is_disabled(self):
		return self.accountstatus == AccountStatus.DISABLED
