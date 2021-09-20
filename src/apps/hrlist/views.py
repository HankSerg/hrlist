from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from src.apps.hrlist.models import Division, Staff


class HomeView(TemplateView):
    # model = Division
    paginate_by = 6
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['divisions'] = Division.objects.all()
        return context
