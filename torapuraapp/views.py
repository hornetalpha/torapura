from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Plan
from .forms import PlanSearchForm
import random
from .models import Post
from django.views.generic import ListView

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

class Post_List_View(ListView):
    template_name = "gallery.html"
    model = Post
    context_object_name = "posts"

class PlanView(TemplateView):
    template_name = "plan.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = PlanSearchForm(self.request.GET or None)
        context['form'] = form
        return context

class PlanResultView(TemplateView):
    template_name = "plan_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = PlanSearchForm(self.request.GET or None)
        if form.is_valid():
            place = form.cleaned_data['place']
            done = form.cleaned_data['done']
            person = form.cleaned_data['person']
            day = form.cleaned_data['day']
            keyword = form.cleaned_data['keyword']
            plans = Plan.objects.filter(place=place, done=done, person=person, day=day)
            if keyword:
                plans = plans.filter(plan_detail__icontains=keyword)
            plans = list(plans)
            if plans:
                context['plan'] = random.choice(plans)
            else:
                context['plan'] = None
            # 選んだ条件をコンテキストに追加
            # doneの値を置き換え
            if done == 'activity':
                done_display = 'スポーツ'
            else:
                done_display = '観光'
            context['selected_conditions'] = {
                'place': place,
                'done': done_display,
                'person': person,
                'day': day,
                'keyword': keyword,
            }
        else:
            context['plan'] = None
            context['selected_conditions'] = {}
        return context
