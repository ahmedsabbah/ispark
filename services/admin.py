from django.contrib import admin
from django import forms
from .models import Tour, Conference, Vacancy, Opportunity

# class TourForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(TourForm, self).__init__(*args, **kwargs)
#         if 'initial' in kwargs:
#              self.fields['majors'].queryset = self.university.majors
#
# class TourAdmin(admin.ModelAdmin):
#     model = Tour
#     form = TourForm(university=)


class ConferenceAdmin(admin.ModelAdmin):
    model = Conference
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
admin.site.register(Conference, ConferenceAdmin)


class TourAdmin(admin.ModelAdmin):
    model = Tour
    list_display = ('university', 'start_date', 'end_date', 'age_range')
    search_fields = ('university__name',)
    list_filter = ('start_date', 'end_date', 'university__name')
admin.site.register(Tour, TourAdmin)


class OpportunityAdmin(admin.ModelAdmin):
    model = Opportunity
    list_display = ('job_title', 'type', 'start_date')
    search_fields = ('job_title', 'type', 'internship_type')
    list_filter = ('type', 'industry')
admin.site.register(Opportunity, OpportunityAdmin)


class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy
    list_display = ('position', 'role')
    search_fields = ('position',)
    list_filter = ('role',)
admin.site.register(Vacancy, VacancyAdmin)
