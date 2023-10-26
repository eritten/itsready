from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# user  profile. it should have  is paid money or not. city, country and phone number and profile picture.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True )
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    company_name = models.CharField(max_length=300, blank=True, null=True)
    is_validated = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return self.user.username

# user credit card information. it should have card number, card holder name, expiration date and cvv.
class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100, blank=True)
    card_holder_name = models.CharField(max_length=100, blank=True, null=True)
    expiration_date = models.CharField(max_length=100, blank=True)
    cvv = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    # user payment history. it should have user, payment date, payment amount and payment status.
class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=timezone.now)
    payment_amount = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
# saving contact information. it should have user, contact name, contact phone number and contact email.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100, blank=True)
    contact_phone_number = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    contact_email = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username
    
   
# this is a sms and voiceMail sending platform. a class for storing sms information.
class Sms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sms_text = models.TextField()
    sms_date = models.DateTimeField(default=timezone.now)
    sms_status = models.BooleanField(default=False)
    contact = models.ManyToManyField(Contact)
    def __str__(self):
        return self.user.username 
    
# this is a sms and voiceMail sending platform. a class for storing voiceMail information.
class VoiceMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voice_mail_text = models.TextField()
    voice_mail_date = models.DateTimeField(default=timezone.now)
    voice_mail_status = models.BooleanField(default=False)
    contact = models.ManyToManyField(Contact)
    def __str__(self):
        return self.user.username

class Privacy(models.Model):
    ip = models.CharField(max_length=100, blank=True)
    area_code = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    country_code = models.CharField(max_length=100, blank=True)
    isp = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    # user has one to one relationship with privacy model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ip
    
class Code(models.Model):
    unique_code = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_generated = models.DateTimeField(default=timezone.now)
    expiring_date = models.DateTimeField()
    def __str__(self):
        return self.unique_code
    
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username