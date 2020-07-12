import uuid

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Group(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='%(class)s_created', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    slug = AutoSlugField(populate_from='name',unique=True)
    description = models.TextField(default='')

    class Meta:
        abstract = True


class Family(Group):
    members = models.ManyToManyField(User, related_name='families')

    class Meta:
        verbose_name_plural = 'families'


class Company(Group):
    members = models.ManyToManyField(User, related_name='companies')

    class Meta:
        verbose_name_plural = 'companies'



INVITE_STATUSES = (
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected')
)


class Invite(models.Model):
    from_user = models.ForeignKey(User, related_name='%(class)s_created')
    to_user = models.ForeignKey(User, related_name='%(class)s_received')
    accepted = models.IntegerField(default=False)
    uuid = models.CharField(max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    # def __str__(self):
    #     return f'{self.to_user} invited by {self.from_user}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = uuid.uuid4().hex
        super().save(*args, **kwargs)

class CompanyInvite(Invite):
    company = models.ForeignKey(Company,related_name='invites')


class FamilyInvite(Invite):
    company = models.ForeignKey(Family, related_name='invites')