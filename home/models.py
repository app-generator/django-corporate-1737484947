# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Rgerg(models.Model):

    #__Rgerg_FIELDS__
    ert = models.CharField(max_length=255, null=True, blank=True)
    tui = models.IntegerField(null=True, blank=True)

    #__Rgerg_FIELDS__END

    class Meta:
        verbose_name        = _("Rgerg")
        verbose_name_plural = _("Rgerg")


class Z5(models.Model):

    #__Z5_FIELDS__
    agr = models.IntegerField(null=True, blank=True)
    weigt = models.TextField(max_length=255, null=True, blank=True)

    #__Z5_FIELDS__END

    class Meta:
        verbose_name        = _("Z5")
        verbose_name_plural = _("Z5")



#__MODELS__END
