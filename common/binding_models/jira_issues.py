

class JiraIssue:

    def __init__(self, expand, fields, id, key):
        self.expand = expand
        self.fields = fields
        self.id = id
        self.key = key

    @classmethod
    def init_from_dict(cls, issue_dict):
        fields = JiraIssueFields.init_from_dict(issue_dict.get('fields'))
        return cls(
            expand=issue_dict.get('expand'),
            fields=fields,
            id=issue_dict.get('id'),
            key=issue_dict.get('key')
        )

class JiraIssueFields:

    def __init__(self, description, summary, time_estimate, time_original_estimate, time_spent):
        self.description = description
        self.summary = summary
        self.time_estimate = time_estimate
        self.time_original_estimate = time_original_estimate
        self.time_spent = time_spent

    @classmethod
    def init_from_dict(cls, fields_dict):
        return cls(
            description=fields_dict.get('description'),
            summary=fields_dict.get('summary'),
            time_estimate=fields_dict.get('timeestimate'),
            time_original_estimate=fields_dict.get('timeoriginalestimate'),
            time_spent=fields_dict.get('timespent')
        )

