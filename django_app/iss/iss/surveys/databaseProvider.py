from iss.surveys import models
from django.contrib.auth.models import User


class DatabaseProvider:
    START_VERSION = 1

    def init(self):
        pass

    def save(self, if_new, name, username, code, js):
        try:
            survey = models.Survey.objects.get(name=name)
            if if_new:
                return 0
            survey.content = code
            survey.result = js
            survey.version += 1
            survey.save()
        except models.Survey.DoesNotExist:
            if if_new:
                survey = models.Survey(
                    name=name, content=code,
                    result=js, version=self.START_VERSION)
                survey.save()
                user = User.objects.get(username=username)
                permission = models.Permission(
                    user_login=user, survey_id=survey)
                permission.save()
        return 1

    def search(self, text, username):
        return map(lambda x: x.survey_id.name,
                   models.Permission.objects.filter(
                       user_login__username=username,
                       survey_id__name__icontains=text))

    def find(self, name):
        return models.Survey.objects.get(
            name=name).content
