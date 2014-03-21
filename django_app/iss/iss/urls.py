from django.conf.urls import patterns, include, url
from iss.surveys.views import SurveyView, TestView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', SurveyView.as_view(), name='survey_view'),
    url(r'^test$', TestView.as_view(), name='test_view'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)
