from django.contrib import admin
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization')

admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Resume)