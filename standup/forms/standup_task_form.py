from django.forms import ModelForm

from models import StandupTask, StandupTaskWork


class StandupTaskForm(ModelForm):
    def get_jira_issue_key(self):
        return self.data.get('jira_issue_key')

    class Meta:
        model = StandupTask
        fields = ('description', 'project', 'jira_issue_key', 'initial_estimate_in_hours')


class StandupTaskWorkForm(ModelForm):
    def get_time_spent_in_hours(self):
        return self.data.get('time_spent_in_hours')

    class Meta:
        model = StandupTaskWork
        fields = ('time_spent_in_hours', 'expected_outcome', 'actual_outcome')