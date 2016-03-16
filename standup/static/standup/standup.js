
$(document).ready(function() {
    var jiraIssueKeyElement = $("#id_jira_issue_key");
    jiraIssueKeyElement.attr("disabled", "disabled");
    $("#jira_issue_dropdown").change(function() {
        var value = this.value;
        jiraIssueKeyElement.val(value);
        debugger;
        $("#id_description").val()
    });
});