from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Group(models.Model, object):
    group_name = models.CharField(max_length=100)
    group_code = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})
