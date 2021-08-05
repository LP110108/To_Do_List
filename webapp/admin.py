from django.contrib import admin
from webapp.models import Task, Status, Type, TaskAdmin, TypeAdmin, StatusAdmin

admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)

