from django.contrib import admin
from django import forms
from .models import Category, Skill, University, Mentor, Contact, Announcement, Partner, TeamMember, Job, JobSkill, Testimonial, SliderSecondary, SliderMain


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    search_fields = ('name',)
admin.site.register(Skill, SkillAdmin)


class UniversityAdmin(admin.ModelAdmin):
    model = University
    search_fields = ('name',)
admin.site.register(University, UniversityAdmin)


class MentorAdmin(admin.ModelAdmin):
    model = Mentor
    search_fields = ('name', 'areas_of_expertise__name')
    list_filter = ('areas_of_expertise__name',)
admin.site.register(Mentor, MentorAdmin)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('type',)
    list_filter = ('type',)
admin.site.register(Contact, ContactAdmin)

class JobSkillInline(admin.TabularInline):
    model = JobSkill
    fk_name = "job"

class JobAdmin(admin.ModelAdmin):
    model = Job
    search_fields = ('title',)
    inlines = (JobSkillInline,)
admin.site.register(Job, JobAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    list_display = ('title', 'author', 'created_date')
    ordering = ('-created_date',)
    list_filter = ('created_date',)
admin.site.register(Announcement, AnnouncementAdmin)

admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(SliderSecondary)
admin.site.register(Partner)

admin.site.register(SliderMain)
