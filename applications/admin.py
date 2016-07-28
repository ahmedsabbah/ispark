from django.contrib import admin
from django import forms
from .models import TourApplication, ConferenceApplication, VacancyApplication, OpportunityApplication

class TourApplicationAdmin(admin.ModelAdmin):
    model = TourApplication
    list_display = ('name', 'school_name', 'grade_level', 'joined_previous_event', 'tour')
    search_fields = ('name',)
    list_filter = ('tour__university__name', 'know_about_us', 'joined_previous_event')
admin.site.register(TourApplication, TourApplicationAdmin)

class ConferenceApplicationAdmin(admin.ModelAdmin):
    model = ConferenceApplication
    list_display = ('name', 'school_name', 'grade_level', 'joined_previous_event', 'conference')
    search_fields = ('name',)
    list_filter = ('conference__name', 'know_about_us', 'joined_previous_event')
admin.site.register(ConferenceApplication, ConferenceApplicationAdmin)

admin.site.register(VacancyApplication)
admin.site.register(OpportunityApplication)
