from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class SchoolCreateView(CreateView):
    model = School
    template_name = "school/school_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('school_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SchoolCreateView, self).form_valid(form)

class SchoolListView(ListView):
    model = School
    template_name = "school/school_list.html"