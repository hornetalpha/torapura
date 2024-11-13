from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    # index.htmlをレンダリングする
    template_name = "index.html"


class GalleryView(TemplateView):
    template_name = "gallery.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class ContactUserView(TemplateView):
    template_name = "contact_user.html"


class ContactCompanyView(TemplateView):
    template_name = "contact_company.html"


class PlanView(TemplateView):
    template_name = "plan.html"
