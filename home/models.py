from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# user  profile. it should have  is paid money or not. city, country and phone number and profile picture.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username

# user credit card information. it should have card number, card holder name, expiration date and cvv.
class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100, blank=True)
    card_holder_name = models.CharField(max_length=100, blank=True)
    expiration_date = models.CharField(max_length=100, blank=True)
    cvv = models.CharField(max_length=100, blank=True)

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
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 
    
# this is a sms and voiceMail sending platform. a class for storing voiceMail information.
class VoiceMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voice_mail_text = models.TextField()
    voice_mail_date = models.DateTimeField(default=timezone.now)
    voice_mail_status = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
 