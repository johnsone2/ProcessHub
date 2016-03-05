from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here

# TODO: Look in to _str_ method for models


class Organization(models.Model):
    name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "organization"


class ApplicationUser(AbstractBaseUser):
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    identifier = models.CharField(max_length=36, unique=True)
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False, null=False)


class StandupTask(models.Model):
    description = models.CharField(max_length=128)
    jira_issue_id = models.IntegerField()
    created_by_user = models.ForeignKey(ApplicationUser, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    initial_estimate_in_hours = models.DecimalField(max_digits=5, decimal_places=2)
    is_completed = models.BooleanField(blank=True, default=False)
    is_blocked = models.BooleanField(blank=True, default=False)
    is_deleted = models.BooleanField(blank=True, default=False)
    is_template = models.BooleanField(blank=True, default=False)

    class Meta:
        db_table = "standup_task"

class StandupTaskWork(models.Model):
    standup_task = models.ForeignKey(StandupTask, on_delete=models.PROTECT)
    time_spent_in_hours = models.DecimalField(max_digits=5, decimal_places=2)
    # todo: use choices validator
    expected_outcome = models.CharField(blank=True, null=True, max_length=64)
    actual_outcome = models.CharField(blank=True, null=True, max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "standup_task_work"
