#from django.shortcuts import render

#from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from gApp.serializers import UserSerializer, ScoreSerializer
from gApp.models import Score


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ScoreViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	automatically provides list and detail actions?
	"""
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer