from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class TextPageView(TemplateView):
    template_name = "text.html"


class ResumePageView(TemplateView):
    template_name = "resume.html"
