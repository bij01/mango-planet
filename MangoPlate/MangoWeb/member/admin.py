from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'pwd', 'rdate']


admin.site.register(Member, MemberAdmin)
