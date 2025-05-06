from rest_framework import viewsets
from .models import Project, Certification, Message,Blog
from .Serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-published_at')
    serializer_class = BlogSerializer

    @action(detail=True, methods=['post'])
    def view(self, request, pk=None):
        blog = self.get_object()
        View.objects.create(blog=blog, ip_address=request.data.get('ip_address'))
        return Response({'status': 'view counted'})

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all().order_by('-uploaded_at')
    serializer_class = ResumeSerializer