from django.contrib import admin
from kiberdb.models import School, Staff, Group, Student, Parent, Schedule, Module


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass
