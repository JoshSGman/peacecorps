from django.db import models
from django.core.urlresolvers import reverse

from apps.worldmap import data_options

class PCVProfile(models.Model):
    is_pcv = models.BooleanField(default=True)
    user = models.OneToOneField('auth.User')
    country = models.CharField("Post Country", choices=data_options.COUNTRY_CHOICES, max_length=128, blank=True)
    sector = models.CharField(choices=data_options.SECTORS, max_length=128, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    home_address = models.CharField(max_length=128, blank=True, default="")
    home_state = models.CharField(choices=data_options.STATES, max_length=128, blank=True, default="")
    bio = models.TextField(blank=True)

    @property
    def blog_url(self):
        return reverse("blog_user_entries", args=[self.user.username])

    def __unicode__(self):
        return self.user.username

    def as_dict(self):
        return {
            'username': self.user.username,
            'name': "%s %s" % (self.user.first_name, self.user.last_name),
            'country': self.country,
            'home_state': self.home_state,
            'id': self.id,
            'sector': self.sector,
        }

class School(models.Model):
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(choices=data_options.STATES, max_length=128, blank=True)
    school_name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10, blank=True)
    about = models.TextField(blank=True)

    def __unicode__(self):
        return self.school_name

    def get_lat_long(self):
        # from zip_code find lat_long
        # return data_options.ZIP_MAP[self.zip_code]
        return (1111, 2222)

    def as_dict(self):
        return {
            'city': self.city,
            'state': self.state,
            'school_name': self.school_name,
            'zip_code': self.zip_code,
            'about': self.about,
            'lat_long': self.get_lat_long(),
        }

class Teacher(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.ForeignKey(School, blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True)
    following = models.ForeignKey('auth.User', related_name='following', blank=True, null=True)
    address = models.CharField(max_length=128, blank=True)
    bio = models.TextField(blank=True)
    def __unicode__(self):
        return self.user.username
