from django.contrib import admin
from django import forms
from .models import Category, Major, Skill, University, Mentor, Contact, Announcement, TeamMember


class MajorInline(admin.TabularInline):
    model = Major
    fk_name = "category"
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ('name',)
    inlines = (MajorInline,)
admin.site.register(Category, CategoryAdmin)


class MajorAdmin(admin.ModelAdmin):
    model = Major
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
admin.site.register(Major, MajorAdmin)


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    search_fields = ('name',)
admin.site.register(Skill, SkillAdmin)


class UniversityAdmin(admin.ModelAdmin):
    model = University
    search_fields = ('name', 'majors__name', 'majors__category__name')
    list_filter = ('majors__category',)
admin.site.register(University, UniversityAdmin)


class MentorAdmin(admin.ModelAdmin):
    model = Mentor
    search_fields = ('name', 'areas_of_expertise__name')
    list_filter = ('areas_of_expertise__name',)# 'areas_of_expertise')
admin.site.register(Mentor, MentorAdmin)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('type',)
    list_filter = ('type',)
admin.site.register(Contact, ContactAdmin)


class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    list_display = ('title', 'author', 'created_date')
    ordering = ('-created_date',)
    list_filter = ('created_date',)
admin.site.register(Announcement, AnnouncementAdmin)

admin.site.register(TeamMember)
