import os

import slumber
from slumber.exceptions import HttpClientError

from common.binding_models.jira_issues import JiraIssue


class JiraClientService:
    def __init__(self):
        self.jira_api = slumber.API(
            os.environ.get("JIRA_API_BASE_URL"),
            append_slash=False,
            auth=(os.environ.get('JIRA_API_USERNAME'), os.environ.get("JIRA_API_PASSWORD"))
        )

    def get_issues_in_project(self, project_key):
        try:
            all_issues_in_der_jql = "project={pid}".format(pid=project_key)
            response = self.jira_api.search.get(jql=all_issues_in_der_jql, max_results=-1)
            jira_issues = [JiraIssue.init_from_dict(issue_dict) for issue_dict in response.get('issues')]
            return jira_issues
        except Exception as e:
            # TODO: Log here
            raise e

    def log_time_on_issue(self, issue_key, time_spent_in_hours):
        update_request = {
            "timeSpentSeconds": time_spent_in_hours * 3600
        }
        self.jira_api.issue(issue_key).worklog.post(update_request)

