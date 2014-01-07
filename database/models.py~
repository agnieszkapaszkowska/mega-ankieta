from django.db.model import models
from django.contrib.auth.models import User


class Survey(models.Model):
    id = models.IntegerField(primaryKey = True, autoincrement = True)
    content = models.TextField()
    result = models.TextField()
    version = models.IntegerField()

    def __unicode__(self):
        return "%d: %d" % (self.id, self.version)

class Permissions(models.Model):
    user_login = models.ForeignKey('User')
    survey_id = models.ForeignKey('Survey')
    
    def __unicode__(self):
        return "%s %d" % (self.user_login.username, self.survey_id.id)

    class Meta:
        unique_together = ("user_login", "survey_id")

