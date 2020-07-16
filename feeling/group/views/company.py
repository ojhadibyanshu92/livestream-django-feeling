from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from braces.views import SetHeadlineMixin
from .. import forms
from ..models import Company
from .. import models


class Create(LoginRequiredMixin,SetHeadlineMixin,generic.CreateView):
    form_class = forms.CompanyForm
    headline= 'Create Company'
    success_url = reverse_lazy('users:dashboard')
    template_name = 'companies/form.html'

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response

class Update(LoginRequiredMixin,SetHeadlineMixin,generic.UpdateView):
    form_class = forms.CompanyForm
    success_url = reverse_lazy('users:dashboard')
    template_name = 'companies/form.html'

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_headline(self):
        return f'Edit {self.object.name}'



class Detail(LoginRequiredMixin,generic.FormView):
    form_class = forms.CompanyInviteForm
    template_name = 'companies/detail.html'

    def get_success_url(self):
        self.get_object()
        return reverse('group:companies:detail', kwargs={
            'slug': self.object.slug})

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_object(self):
        self.object = self.request.user.companies.get(
            slug=self.kwargs.get('slug')
        )
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        models.CompanyInvite.objects.create(
            from_user=self.request.user,
            to_user=form.invitee,
            company=self.get_object()
        )
        return response


class Invites(LoginRequiredMixin, generic.ListView):
    model = models.CompanyInvite
    template_name = 'companies/invites.html'

    def get_queryset(self):
        return self.request.user.companyinvite_received.filter(status=0)


class InviteResponse(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('group:companies:invites')

    def get(self, request, *args, **kwargs):
        invite = get_object_or_404(
            models.CompanyInvite,
            to_user=request.user,
            uuid=kwargs.get('code'),
            status=0
        )
        if kwargs.get('response') == 'accept':
            invite.status = 1
        else:
            invite.status = 2

        invite.save()

        return super().get(request, *args, **kwargs)


