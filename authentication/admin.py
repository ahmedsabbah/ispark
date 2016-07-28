from django.contrib import admin
from models import Profile, Badge
# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Badge)

class BadgeInline(admin.TabularInline):
    model = Badge
    fk_name = "profile"
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ('user__first_name', 'user__last_name', 'user__email',)
    inlines = (BadgeInline,)
admin.site.register(Profile, ProfileAdmin)
