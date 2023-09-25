from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# receiver for ssending mail to user after registration, but avoid update on user when user is updated

@receiver(post_save, sender=User)
def mail(sender, instance, created, **kwargs):
    if created:
        instance.email_user("Welcome to itsready", "Thank you for registering on itsready app.")
                            
                            
                            
