from django.contrib import admin
from iss.surveys.models import Survey, Permission, Attachment

class SurveyAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(SurveyAdmin, self).queryset(request)
        ids = map(lambda p: p.survey_id.pk,
                  Permission.objects.filter(
                      user_login=request.user))
        return qs.filter(pk__in=ids)


class PermissionAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(PermissionAdmin, self).queryset(request)
        return qs.filter(user_login=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'survey_id':
            ids = map(lambda p: p.survey_id.pk,
                      Permission.objects.filter(
                          user_login=request.user))
            kwargs['queryset'] = Survey.objects.filter(pk__in=ids)
        return super(PermissionAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Attachment)
