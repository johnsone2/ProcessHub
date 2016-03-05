from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here

# TODO: Look in to _str_ method for models
from authentication.models import ApplicationUser


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
