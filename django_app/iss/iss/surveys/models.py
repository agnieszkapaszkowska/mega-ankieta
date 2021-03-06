import os
from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    result = models.TextField()
    version = models.IntegerField()

    def __unicode__(self):
        return "%s: %d" % (self.name, self.version)


class Permission(models.Model):
    user_login = models.ForeignKey(User)
    survey_id = models.ForeignKey('Survey')

    def __unicode__(self):
        return "%s %d" % (self.user_login.username, self.survey_id.id)

    class Meta:
        unique_together = ("user_login", "survey_id")


class Attachment(models.Model):
    file_field = models.FileField(
        upload_to=os.path.abspath(os.path.dirname(__file__)) + "/attachment",
        blank=True)

    def __unicode__(self):
        return unicode(unicode(self.file_field).split("/")[-1])
