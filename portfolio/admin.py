from django.contrib import admin
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Project, ProjectImage, Certification, Message, Blog, Like, Comment, View, Resume


# -------- Forms --------
class ProjectAdminForm(forms.ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Project
        fields = '__all__'


class CertificationAdminForm(forms.ModelForm):
    logo = CloudinaryFileField()

    class Meta:
        model = Certification
        fields = '__all__'


class BlogAdminForm(forms.ModelForm):
    cover_image = CloudinaryFileField()

    class Meta:
        model = Blog
        fields = '__all__'


class ProjectImageInlineForm(forms.ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = ProjectImage
        fields = '__all__'


# -------- Inlines --------
class ProjectImageInline(admin.TabularInline):
    form = ProjectImageInlineForm
    model = ProjectImage
    extra = 1  # Number of empty forms to display


# -------- Admins --------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'tags')
    inlines = [ProjectImageInline]


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


# Register remaining models without custom admin
admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Resume)
