from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from app.models import *

admin.site.site_header = 'Tech Melange'
admin.site.site_url = None

admin.site.unregister(Group)


@admin.register(TechFest)
class TechFestAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    show_full_result_count = True
    list_display = ('name', 'start_date', 'end_date')

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('name', 'event_start_date', 'event_end_date')

@admin.register(StudentCoordinators)
class StudentCoordinatorsAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('name',)

@admin.register(TeacherCoordinators)
class TeacherCoordinatorsAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('name',)

@admin.register(StudentCouncilMembers)
class StudentCouncilMembersAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('name','position')

@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('name',)

@admin.register(Sponsors)
class SponsorsAdmin(admin.ModelAdmin):
    show_full_result_count = True
    list_display = ('name',)
