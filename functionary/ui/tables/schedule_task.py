import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html

from core.models.scheduled_task import ScheduledTask


class ScheduledTaskTable(tables.Table):
    name = tables.Column(
        linkify=lambda record: reverse(
            "ui:scheduledtask-detail", kwargs={"pk": record.id}
        ),
    )
    function = tables.Column(
        linkify=lambda record: reverse(
            "ui:function-detail", kwargs={"pk": record.function.id}
        ),
    )
    last_run = tables.DateTimeColumn(
        accessor="most_recent_task__created_at",
        verbose_name="Last Run",
        linkify=lambda record: reverse(
            "ui:task-detail", kwargs={"pk": record.most_recent_task}
        ),
        format="N j, Y, g:i a",
    )
    schedule = tables.Column(accessor="periodic_task__crontab", verbose_name="Schedule")
    edit_button = tables.Column(
        accessor="id",
        verbose_name="",
    )

    class Meta:
        model = ScheduledTask
        fields = ("name", "function", "last_run", "schedule", "status", "edit_button")
        attrs = {"class": "table is-striped is-hoverable is-fullwidth"}

    def render_edit_button(self, value, record):
        return format_html(
            f'<a href="{reverse("ui:scheduledtask-update", kwargs={"pk": record.id})}">'
            f'<button class="button is-small has-text-link is-white singletonActive">'
            f'<span class="fa fa-pencil-alt"></span>'
            f"</button></a>"
        )
