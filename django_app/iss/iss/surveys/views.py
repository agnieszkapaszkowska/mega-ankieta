from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from iss.surveys.survey import Survey
from iss.surveys.databaseProvider import DatabaseProvider
import json
import sys
import traceback


class SurveyView(TemplateView):
    template_name = 'surveys/index.html'
    GENERATE_TYPE = '1'
    SAVE_TYPE = '2'
    SEARCH_TYPE = '3'
    OPEN_TYPE = '4'

    def post(self, request, *args, **kwargs):
        result = {}

        if request.is_ajax():
            if request.POST['type'] == self.GENERATE_TYPE:
                Survey.text = ' ' + request.POST['input'] + ' '
                error, survey = Survey.generate()

                result['survey'] = survey
                result['error'] = error

            elif request.POST['type'] == self.SAVE_TYPE:
                provider = DatabaseProvider()
                result['success'] = provider.save(
                    request.POST['new'] == '1',
                    request.POST['name'],
                    request.POST['user'],
                    request.POST['code'],
                    request.POST['js'])

            elif request.POST['type'] == self.SEARCH_TYPE:
                provider = DatabaseProvider()
                result['results'] = ';'.join(
                    provider.search(request.POST['text'],
                                    request.POST['username']))

            elif request.POST['type'] == self.OPEN_TYPE:
                provider = DatabaseProvider()
                result['survey'] = provider.find(
                    request.POST['name'])

        return HttpResponse(json.dumps(result),
                            content_type="application/json")


class TestView(TemplateView):
    template_name = 'tests/tests.html'
