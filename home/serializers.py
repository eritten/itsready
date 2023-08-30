from .models import Sms, VoiceMail, Contact
# importing the serializers
from rest_framework import serializers

from django.contrib.auth.models import User

# serializer for user
class UserSerializer(serializers.ModelSerializer):
    # user has one to many relationship with contact 
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

# creating a serializer for contact model. it has one to many relationship with user model
class ContactSerializer(serializers.ModelSerializer):
    # user has one to many relationship with contact model
#    user = serializers.ReadOnlyField(source='user.username')
# use string related field to create the relationshi
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'user',  'contact_phone_number', 'contact_email', 'contact_name']

# creating a serializer for sms model. it has one to many relationship with user model
class SmsSerializer(serializers.ModelSerializer):
    # user has one to many relationship with sms model
#    user = serializers.ReadOnlyField(source='user.username')
    user = serializers.StringRelatedField(read_only=True)
    # contact has many to many relationship with sms model
#    contact = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())
    contact = ContactSerializer(many=True, read_only=True)
    class Meta:
        model = Sms
        fields = ['id', 'user', 'message', 'date', 'contact']
        
# creating a serializer for voicemail model. it has one to many relationship with user model. it has one to one relationship with contact model
class VoiceMailSerializer(serializers.ModelSerializer):
    # user has one to many relationship with sms model
#    user = serializers.ReadOnlyField(source='user.username')
    user = serializers.StringRelatedField(read_only=True)
    # contact has many to many relationship with sms model
#    contact = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())
    contact = ContactSerializer(many=True, read_only=True)
    class Meta:
        model = VoiceMail
        fields = ['id', 'user', 'contact', 'message', 'date', 'contact']
        
