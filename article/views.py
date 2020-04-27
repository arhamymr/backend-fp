from django.contrib.auth.models import User, Group
from .models import Articles
from rest_framework import viewsets, permissions
from article.serializers import UserSerializer, GroupSerializer, ArticleSerializer
from rest_framework.parsers import FileUploadParser

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited 
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	# permission_classes = [permissions.isAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Articles.objects.all()
	serializer_class = ArticleSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoit that allows group to be viewed or edited
	"""
	queryset = User.objects.all()
	serializer_class = GroupSerializer
	# permission_classes = [permissions.isAuthenticated]

