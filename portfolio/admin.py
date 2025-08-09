from django.contrib import admin
from .models import Project, ProjectImage, Certification, Message, Blog, Like, Comment, View, Resume

# Inline for additional project images
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # How many empty fields to show by default


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'tags')
    inlines = [ProjectImageInline]  # Allows adding extra images inside Project edit page


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'date')
    search_fields = ('title', 'organization')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'description')


admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Resume)
