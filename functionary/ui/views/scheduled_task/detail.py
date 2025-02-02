from core.models import Task
from core.models.scheduled_task import ScheduledTask
from ui.views.generic import PermissionedDetailView


class ScheduledTaskDetailView(PermissionedDetailView):
    model = ScheduledTask

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scheduledtask: ScheduledTask = context["scheduledtask"]
        history = Task.objects.filter(scheduled_task=scheduledtask).order_by(
            "-created_at"
        )[:10]
        context["history"] = history
        return context
