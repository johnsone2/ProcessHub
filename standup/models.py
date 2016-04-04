from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here

# TODO: Look in to _str_ method for models
from authentication.models import ApplicationUser


class Project(models.Model):
    name = models.CharField(max_length=64)
    jira_project_key = models.CharField(max_length=128, null=True, blank=True)
    created_by_user = models.ForeignKey(ApplicationUser, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"
        unique_together = ('name',)


class StandupTask(models.Model):
    description = models.CharField(max_length=128)
    jira_issue_key = models.CharField(max_length=128, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created_by_user = models.ForeignKey(ApplicationUser, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    initial_estimate_in_hours = models.DecimalField(max_digits=5, decimal_places=2)
    is_completed = models.BooleanField(blank=True, default=False)
    is_blocked = models.BooleanField(blank=True, default=False)
    is_deleted = models.BooleanField(blank=True, default=False)

    class Meta:
        db_table = "standup_task"


class StandupTaskWork(models.Model):
    standup_task = models.ForeignKey(StandupTask, on_delete=models.PROTECT)
    description = models.CharField(max_length=1028)
    time_spent_in_hours = models.DecimalField(max_digits=5, decimal_places=2)
    expected_outcome_choices = [('will_finish', 'Will Finish'), ('wont_finish', "Won't Finish")]
    expected_outcome = models.CharField(blank=True, null=True, max_length=64, choices=expected_outcome_choices)
    actual_outcome_choices = [('did_finish', 'Finished'), ('did_not_finish', 'Did not Finish')]
    actual_outcome = models.CharField(blank=True, null=True, max_length=64, choices=actual_outcome_choices)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "standup_task_work"
