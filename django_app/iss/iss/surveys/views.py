from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from iss.surveys.survey import Survey
import json

class SurveyView(TemplateView):
    template_name = 'surveys/index.html'
    GENERATE_TYPE = '1'
    SAVE_TYPE = '2'

    def post(self, request, *args, **kwargs):
        result = {}

        if request.is_ajax():
            if request.POST['type'] == self.GENERATE_TYPE:
                Survey.text = request.POST['input']
                error, survey = Survey.generate()

                result['survey'] = survey
                result['error'] = error

        return HttpResponse(json.dumps(result),
                                    content_type="application/json")
