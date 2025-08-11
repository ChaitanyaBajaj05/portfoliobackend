from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from portfolio.views import (
    ProjectViewSet,
    CertificationViewSet,
    MessageViewSet,
    BlogViewSet,
    LikeViewSet,
    CommentViewSet,
    ResumeViewSet,
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet,basename='projects')
router.register(r'certifications', CertificationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'resumes', ResumeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Only serve media files locally in development
# In production, Cloudinary handles all media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
