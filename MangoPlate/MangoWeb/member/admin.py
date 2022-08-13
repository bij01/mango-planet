from django.contrib import admin
from .models import Member, Qna


class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'pwd', 'rdate']


class QnaAdmin(admin.ModelAdmin):
    list_display = ['writer', 'comment', 'rdate']


admin.site.register(Member, MemberAdmin)
admin.site.register(Qna, QnaAdmin)
