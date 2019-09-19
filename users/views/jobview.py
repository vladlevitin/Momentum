from django.shortcuts import render

from django.views.generic import (DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin,     #The user can only create a post if logged in
                                        UserPassesTestMixin)    #Only the author can update the post
from django.views.generic import ListView
from django.apps import apps
from django.contrib import messages

from django.shortcuts import render, redirect


Job = apps.get_model('users', 'Job')
Type = apps.get_model('users', 'Type')
Pub_or_priv = apps.get_model('users', 'Pub_or_priv')
Field = apps.get_model('users', 'Field')



def browse(request):
    context = {
        'jobs': Job.objects.all(),
        'all_types': Type.objects.all(),
        'all_pop': Pub_or_priv.objects.all(),
        'all_fields': Field.objects.all()
    }
    return render(request, 'jobs/browse.html', context)


class JobDetailView(DetailView):                                            #view for detail of each job
    model=Job
    template_name = 'jobs/job_detail.html'


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):   #view for deleting a spesific job
    model=Job
    success_url = '/jobs/browse/'
    template_name = 'jobs/job_confirm_delete.html'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.employer:                                #checks if the user trying to delete the post is the author of the post
            return True
        return False


class JobCreateView(LoginRequiredMixin, CreateView):                        #view for creating a new job publication
    model=Job
    fields = ['email','position', 'description','deadline','type','start']
    template_name = 'jobs/job_form.html'


    def form_valid(self, form):
        form.instance.employer = self.request.user                          # setting the employer of the post to user
        return super().form_valid(form)                                     # returns the form

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.employer:                              # checks if the user trying to update the post is the author of the post
            return True
        return False

    def form_valid(self, form):
        form.instance.employer = self.request.user                          #setting the employer of the post to user
        return super().form_valid(form)                                     #returns the form


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   #view for updating a new job publication
    model=Job
    fields = ['email','position', 'description','deadline','type','start']
    template_name = 'jobs/job_form.html'

    def form_valid(self, form):
        form.instance.employer = self.request.user                          #setting the employer of the post to user
        return super().form_valid(form)                                     #returns the form

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.employer:                                #checks if the user trying to update the post is the author of the post
            return True
        return False
