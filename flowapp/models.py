from django.db import models
from django_enumfield import enum
from django_extensions.db import models as models_ext


class AccountType(enum.Enum):
    ROLE = 0
    USER = 1


class AccountStatus(enum.Enum):
    ENABLED = 0
    DISABLED = 1


class Account(models_ext.TimeStampedModel):
    """Account is someone that might author content

    This might be a person or a role account or some other account type that we
    don't have today.
    """
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    api_key = models.CharField(max_length=128)
    accounttype = enum.EnumField(AccountType, default=AccountType.USER)
    accountstatus = enum.EnumField(AccountStatus, default=AccountStatus.ENABLED)
    topic = models.ForeignKey('Topic')

    def is_user(self):
        return self.accounttype == AccountType.USER

    def is_role_account(self):
        return self.accounttype == AccountType.ROLE

    def is_enabled(self):
        return self.accountstatus == AccountStatus.ENABLED

    def is_disabled(self):
        return self.accountstatus == AccountStatus.DISABLED


class Topic(models_ext.TimeStampedModel):
    """Topic is the unit of organization of content

    Right now you can't delete or hide topics. This is by design.
    """
    name = models.CharField(max_length=128, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    tags = models.ManyToManyField('Tag')


class Tag(models_ext.TimeStampedModel):
    """Tags are used in various places as metadata

    """
    name = models.CharField(max_length=128, unique=True)


class Event(models_ext.TimeStampedModel):
    """Events are the core bit of information

    Think of them as tweets. They carry a payload of text, some tags, and are
    published within a Topic.

    We presently don't support any type of event deletion or hiding. What's
    published stays forever... for now.
    """
    author = models.ForeignKey('Account', null=True)
    topic = models.ForeignKey('Topic')
    tags = models.ManyToManyField('Tag')
    content = models.TextField()
