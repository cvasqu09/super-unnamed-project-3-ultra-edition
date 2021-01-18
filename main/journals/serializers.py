from rest_framework import serializers
from journals.models import Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'title', 'createdAt', 'content', 'user']