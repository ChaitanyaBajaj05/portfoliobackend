from rest_framework import serializers
from .models import *
from cloudinary import CloudinaryImage

class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']
    
    def get_image(self, obj):
        if obj.image:
            # Return the Cloudinary URL
            return str(obj.image.url)
        return None

class ProjectSerializer(serializers.ModelSerializer):
    additional_images = ProjectImageSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            # Return the Cloudinary URL
            return str(obj.image.url)
        return None



class CertificationSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    
    class Meta:
        model = Certification
        fields = '__all__'
    
    def get_logo(self, obj):
        if obj.logo:
            # Return the Cloudinary URL
            return str(obj.logo.url)
        return None


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            'id', 
            'title', 
            'description', 
            'cover_image', 
            'published_at', 
            'link',
            'likes_count',
            'views_count',
            'comments'
        ]

    def get_cover_image(self, obj):
        if obj.cover_image:
            # Return the Cloudinary URL
            return str(obj.cover_image.url)
        return None

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_views_count(self, obj):
        return obj.views.count()

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'text', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'name', 'file', 'uploaded_at']