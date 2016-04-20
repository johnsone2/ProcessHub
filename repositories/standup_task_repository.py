from django.db.models import Prefetch

from standup.models import StandupTask, StandupTaskWork


class StandupTaskRepository(object):
    def get_all_standup_tasks_for_org(self, org_id):
        # TODO: Possibly add prefetch
        return StandupTask.objects.filter(created_by_user__organization_id=org_id)

    def get_standup_tasks_for_user(self, user_id):
        prefetch = Prefetch(
            'standuptaskwork_set',
            queryset=StandupTaskWork.objects.order_by('-date_created'),
            to_attr='work'
        )
        return StandupTask.objects.filter(created_by_user_id=user_id).prefetch_related(prefetch)

    def get_standup_task(self, standup_task_id):
        return StandupTask.objects.get(pk=standup_task_id)

    def create_standup_task(self, standup_task_model):
        standup_task_model.save()
        return standup_task_model

    def create_standup_task_work(self, standup_task_work_model):
        standup_task_work_model.save()
        return standup_task_work_model


