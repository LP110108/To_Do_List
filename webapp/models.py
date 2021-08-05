from django.db import models
from django.contrib import admin


class Task(models.Model):
    summary = models.TextField(max_length=64, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    created_at = models.DateTimeField(max_length=30, null=True, verbose_name='Useless')


def __str__(self):
    return "{}. {}".format(self.pk, self.title)


class Status(models.Model):
    status = models.ForeignKey(Task, related_name='status', on_delete=models.PROTECT, verbose_name='Status')
    all_statuses = models.CharField(
        max_length=16,
        choices=(
            ('new', 'new'),
            ('in_progress', 'in_progress'),
            ('pause', 'pause'),
            ('done', 'done')
        ),
        default='new'
    )


class Type(models.Model):
    type = models.ForeignKey(Task, related_name='type', on_delete=models.PROTECT, verbose_name='Type')
    all_types = models.CharField(
        max_length=16,
        choices=(
            ('task', 'task'),
            ('bug', 'bug'),
            ('enchantment', 'enchantment'),
            ('research', 'research')
        ),
        default='task'
    )


class TaskAdmin(admin.ModelAdmin):
	list_display = ['summary']
	list_filter = ['summary', 'created_at']
	search_fields = ['summary', 'created_at']
	fields = ['summary', 'description', 'created_at']
	readonly_fields = []


class StatusAdmin(admin.ModelAdmin):
	list_display = ['all_statuses']
	list_filter = ['all_statuses', 'status']
	search_fields = ['all_statuses', 'status']
	fields = ['all_statuses']
	readonly_fields = []


class TypeAdmin(admin.ModelAdmin):
	list_display = ['all_types']
	list_filter = ['all_types', 'type']
	search_fields = ['all_types', 'type']
	fields = ['all_types']
	readonly_fields = []
