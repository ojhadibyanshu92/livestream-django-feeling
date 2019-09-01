from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.views.generic import FormView,CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

def dashboard(request):
    return render(request,'users/dashboard.html')

class LogoutView(LoginRequiredMixin,FormView):
    form_class = forms.LogoutForm
    template_name='users/logout.html'
    def form_valid(self,form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:dashboard')

