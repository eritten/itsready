from .models import Sms, VoiceMail, Contact
# importing the serializers
from rest_framework import serializers

from django.contrib.auth.models import User

# creating a serializer for sms model. it has one to many relationship with user model
class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = ['id', 'user', 'message', 'date', 'contact']
        
# creating a serializer for voicemail model. it has one to many relationship with user model. it has one to one relationship with contact model
class VoiceMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceMail
        fields = ['id', 'user', 'contact', 'message', 'date', 'contact']
        
# creating a serializer for contact model. it has one to many relationship with user model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user',  'contact_phone_number', 'contact_email', 'contact_name']