from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PalindromeModel

class PalindromeHistorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PalindromeModel
    fields = ['string', 'isPalindrome', 'added_on']