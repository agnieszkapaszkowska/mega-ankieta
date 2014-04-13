from django.contrib import admin
from iss.surveys.models import Survey, Permission, Attachment


admin.site.register(Survey)
admin.site.register(Permission)
admin.site.register(Attachment)
