from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Startup, Investor, Person


# Creates profile if User instance is created. Admin defined as Person.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if instance.is_startup and created:
        print('Startup profile generation OK')
        Startup.objects.create(user=instance)
    elif instance.is_investor and created:
        print('Investor profile generation OK')
        Investor.objects.create(user=instance)
    elif created:
        print('Person/superuser profile generation OK')
        Person.objects.create(user=instance)
    else:
        print(created)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    if instance.is_startup:
        instance.startup_profile.save()
    elif instance.is_investor:
        instance.investor_profile.save()
    else:
        instance.person_profile.save()
