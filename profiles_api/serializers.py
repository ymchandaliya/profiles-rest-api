from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    '''serializer for Profile Model'''
    name = serializers.CharField(max_length=10)
