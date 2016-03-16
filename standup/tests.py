from django.test import TestCase

# Create your tests here.
from services.jira_client_service import JiraClientService


class JiraTests(TestCase):

    def test_hit_jira_api(self):
        client = JiraClientService()

        response = client.get_issue()

        blah = "blah"