from django.conf.urls import patterns, include, url
from iss.surveys.views import SurveyView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', SurveyView.as_view(), name='survey_view'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)
