from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Python', 'Python Apps'),
        ('Full-Stack', 'Full-Stack Apps'),
        ('Graphic Design', 'Graphic Design'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')  # Main Image
    tags = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Full-Stack')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/additional/')

    def __str__(self):
        return f"Image for {self.project.title}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date = models.DateField()
    logo = models.ImageField(upload_to='certifications/')
    certificate_link = models.URLField()

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class Resume(models.Model):
    name = models.CharField(max_length=100, default="Resume")
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='blogs/')
    published_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class View(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField()
    viewed_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
