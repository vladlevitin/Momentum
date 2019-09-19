from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from PIL import Image
from geoposition.fields import GeopositionField

class User(AbstractUser):
    is_startup = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    is_person = models.BooleanField(default=False)


# All created entities of startup, investor and person types are profiles
class Startup(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, related_name='startup_profile')
    name = models.CharField(verbose_name=('Navn'),max_length=50)
    image = models.ImageField(verbose_name=('Profilbilde'), default='default.jpg', upload_to='profile_pics')
    USERNAME_FIELD = 'username'
    sector = models.ForeignKey('Sector',verbose_name=('Sektor'), max_length=50, on_delete=None, null=True)              # public or private
    address = models.CharField(verbose_name=('Adresse'),max_length=200, null=True)
    startup_link = models.URLField(verbose_name=('Hjemmeside'),null=True)                                               # Can add URL link to their own homepage
    industry = models.ForeignKey('Industry',verbose_name=('Industri'), max_length=100, on_delete=None, null=True)
    status = models.ForeignKey('Status', max_length=100, on_delete=None, null=True)
    employees = models.IntegerField(verbose_name=('Antall ansatt'),null=True)                                           # how many employees
    bio = models.TextField(max_length=1000, null=True)
    ceo = models.CharField(verbose_name=('CEO'),max_length=50, null=True)
    latitude = models.FloatField(verbose_name=('Breddegrad'),max_length=20, null=True)
    longitude = models.FloatField(verbose_name=('Lengdegrad'),max_length=20, null=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    # for resizing the image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Investor(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, related_name='investor_profile')
    name = models.CharField(verbose_name=('Navn'), max_length=50)
    image = models.ImageField(verbose_name=('Profilbilde'),default='default.jpg', upload_to='profile_pics')
    USERNAME_FIELD = 'username'
    bio = models.TextField(verbose_name=('Bio'),max_length=500, null=True)
    address = models.CharField(verbose_name=('Adresse'),max_length=200, null=True)
    email2 = models.EmailField(verbose_name=('Kontaktperson (e-mail)'),max_length=100, null=True)                       # Can add link to contact person's email or company email
    investor_link = models.URLField(verbose_name=('Hjemmeside'),null=True)                                              # Can add URL link to their own homepage
    interest = models.CharField(verbose_name=('Interesser'),max_length=50, null=True)                                   # The status the startups they want to invest in are in, ex startup phase, middle phase(?) ect
    status_interest = models.ForeignKey('Status_interest', max_length=100, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField(verbose_name=('Breddegrad'),max_length=20, null=True)
    longitude = models.FloatField(verbose_name=('Lengdegrad'),max_length=20, null=True)
    REQUIRED_FIELDS = []




    def __str__(self):
        return self.name

    # for resizing the image
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Status_interest(models.Model):
    tag = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.tag


class Person(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, related_name='person_profile')
    name = models.CharField(verbose_name=('Navn'),max_length=50)
    image = models.ImageField(verbose_name=('Profilbilde'), default='default.jpg', upload_to='profile_pics')
    USERNAME_FIELD = 'username'
    birthday = models.DateField(verbose_name=('Født (åååå-mm-dd)'),auto_now=False, null=True)
    occupation = models.CharField(verbose_name=('Yrkesstatus'),max_length=100, null=True)
    address = models.CharField(verbose_name=('Adresse'),max_length=200, null=True)
    bio = models.TextField(max_length=500, null=True)

    #EDUCATION
    edu_started = models.DateField(verbose_name=('Startet (åååå-mm-dd)'), null=True)
    edu_ended = models.DateField(verbose_name=('Sluttet (åååå-mm-dd)'), null=True)                                      # If ongoing then choose when education is planned to end
    edu_location = models.CharField(verbose_name=('Utdanningssted'), max_length=200, null=True)                         # Ex NTNU
    edu_title = models.CharField(verbose_name=('Tittel'), max_length=200, null=True)                                    # Ex Datateknologi
    edu_type = models.CharField(verbose_name=('Grad'), max_length=50, null=True)                                        # Ex Master, Bachelor etc

    #WORK EXPERIENCE
    work_employer = models.CharField(verbose_name=('Arbeidsgiver'), max_length=100, null=True)                          # Ex NTNU, Bunnpris
    work_position = models.CharField(verbose_name=('Stillingstittel'), max_length=100, null=True)                       # Job title
    work_description = models.TextField(verbose_name=('Beskrivelse'), max_length=250, null=True)                        # Job description
    work_type = models.CharField(verbose_name=('Stillingstype'), max_length=50, null=True)                              # Full time or part time job

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    # for resizing the image
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Industry(models.Model):
    tag = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.tag


class Sector(models.Model):
    tag = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.tag


class Status(models.Model):
    tag = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.tag

#Jobs stuff, putting in sector, industry and status in Jobs because couldn't figure out how to sort on foreign key attributs

class Job(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer')
    email = models.CharField(max_length=100, null=True)                                                                 # Can add link to contact person's email
    position = models.CharField(verbose_name=('Stilling'),max_length=100, null=True)                                    # Job title
    description = models.TextField(verbose_name=('Beskrivelse'),max_length=250, null=True)                              # Job description
    deadline = models.DateField(verbose_name=('Søknadsfrist'),auto_now=False, null=True)                                # Application deadline
    type = models.ForeignKey('Type', max_length=100, on_delete=None, null=True)                                         # Full time or part time job
    start = models.CharField(verbose_name=('Starttidspunkt'),max_length=50, null=True)                                  # Ex immediately, after christmas, ect
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    pub_or_priv = models.ForeignKey('Pub_or_priv', max_length=50, on_delete=None, null=True, related_name='sector')     # public or private
    field = models.ForeignKey('Field', max_length=100, on_delete=None, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})


class Type(models.Model):
    tag = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.tag


class Pub_or_priv(models.Model):
    tag = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.tag

class Field(models.Model):
    tag = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.tag