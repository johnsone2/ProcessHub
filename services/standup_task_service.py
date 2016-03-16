from django.core.exceptions import ValidationError

from repositories.standup_task_repository import StandupTaskRepository
from services.jira_client_service import JiraClientService


class StandupTaskService():
    def __init__(self):
        self.standup_task_repository = StandupTaskRepository()
        self.jira_client_service = JiraClientService()

    def create_standup_task_with_work(self, standup_task_form, standup_task_work_form, created_by_user):
        if not standup_task_form.is_valid() or not standup_task_form.is_valid():
            errors = {}
            for key, value in standup_task_form.errors.items():
                errors[key] = value[0]
            for key, value in standup_task_work_form.errors.items():
                errors[key] = value[0]
            raise ValueError(errors)

        standup_task_form.instance.created_by_user = created_by_user
        standup_task = self.standup_task_repository.create_standup_task(standup_task_form.instance)

        standup_task_work_form.instance.standup_task = standup_task
        standup_task_work = self.standup_task_repository.create_standup_task(standup_task_work_form.instance)
        if standup_task_form.get_jira_issue_key():
            self.jira_client_service.log_time_on_issue(
                standup_task_form.get_jira_issue_key(),
                standup_task_work_form.get_time_worked_in_hours()
            )

        return standup_task.id

    def get_all_standup_tasks_for_org(self,org_id):
        if not org_id is int:
            raise ValueError("org_id must be an integer")

        return self.standup_task_repository.get_all_standup_tasks_for_org(org_id)

    def get_standup_tasks_for_user(self, user_id):
        if not user_id is int:
            raise ValueError("user_id must be an integer")

        return self.standup_task_repository.get_standup_tasks_for_user(user_id)

    def get_standup_task(self, standup_task_id):
        pass
