from django.views.generic import TemplateView

class HelloWorld(TemplateView):
    template_name = 'tests.html'
