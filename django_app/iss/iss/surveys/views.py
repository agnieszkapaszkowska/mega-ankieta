from django.shortcuts import render
from django.views.generic import TemplateView


class SurveyView(TemplateView):
    template_name = "surveys/index.html"
