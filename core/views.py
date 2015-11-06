from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
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


class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'


    def get_context_data(self, **kwargs):
        context = super(SchoolDetailView, self).get_context_data(**kwargs)
        school = School.objects.get(id=self.kwargs['pk'])
        reviews = Review.objects.filter(school=school)
        context['reviews'] = reviews
        return context

class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school/school_form.html'
    fields = ['title', 'description']

class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school/school_confirm_delete.html'
    success_url = reverse_lazy('school_list')

class ReviewCreateView(CreateView):
    model = Review
    template_name = "review/review_form.html"
    fields = ['text']

    def get_success_url(self):
        return self.object.school.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.school = School.objects.get(id=self.kwargs['pk'])
        return super(ReviewCreateView, self).form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    pk_url_kwarg = 'review_pk'
    template_name = 'review/review_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.school.get_absolute_url()

class ReviewDeleteView(DeleteView):
    model = Review
    pk_url_kwarg = 'review_pk'
    template_name = 'review/review_confirm_delete.html'

    def get_success_url(self):
        return self.object.school.get_absolute_url()

