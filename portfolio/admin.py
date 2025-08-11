from django.contrib import admin
from .models import Project, ProjectImage, Certification, Message, Blog, Like, Comment, View, Resume
from cloudinary.forms import CloudinaryFileField
from django import forms

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'image': CloudinaryFileField(),
        }

class CertificationAdminForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'
        widgets = {
            'logo': CloudinaryFileField(),
        }

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'cover_image': CloudinaryFileField(),
        }

# Inline for additional project images
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # How many empty fields to show by default


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'tags')
    inlines = [ProjectImageInline]  # Allows adding extra images inside Project edit page


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    form = CertificationAdminForm
    list_display = ('title', 'organization', 'date')
    search_fields = ('title', 'organization')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'published_at')
    search_fields = ('title', 'description')


admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Resume)
