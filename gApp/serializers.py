from django.contrib.auth.models import User
from gApp.models import Score
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Score
		fields = ('Course', 'Score', 'Date')