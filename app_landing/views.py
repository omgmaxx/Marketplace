from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from app_catalog.models import Category


class MainPage(TemplateView):
    template_name = 'landing/main.html'
