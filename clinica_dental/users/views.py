from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView, FormView, UpdateView, ListView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.db.models import Sum

from users.models import Profile
from users.forms import SignUpForm, EditUserForm
from appointments.models import Appointments, Consultations, WorkBlocks
from medical_records.models import AccountStatus, MedicalRecords


# --- USER --- #


class LoginView(auth_views.LoginView):

    template_name = 'users/login.html'


class SignUpView(FormView):

    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


class LogOutView(LoginRequiredMixin, auth_views.LogoutView):

    template_name = 'users/logged_out.html'


class SuperUserView(LoginRequiredMixin, ListView):

    template_name = 'users/superuser.html'
    model = Profile
    ordering = ('-user')
    context_object_name = 'users'


class EditUserView(LoginRequiredMixin, UpdateView):

    template_name = 'users/edit_user.html'
    model = Profile
    form_class = EditUserForm
    success_url = reverse_lazy('users:superuser')


# ---  STATISTICS --- #


class StatisticsFeedView(LoginRequiredMixin, ListView):

    template_name = 'users/statistics.html'
    model = Appointments
    context_object_name = 'appointments'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['consultations'] = Consultations.objects.all()
        context['bills'] = AccountStatus.objects.all()
        context['records'] = MedicalRecords.objects.all()

        context['total_appointments'] = Appointments.objects.count()
        context['standby_appointments'] = Appointments.objects.filter(status = 'Stand By').count()
        context['cancel_appointments'] = Appointments.objects.filter(status = 'Cancel').count()
        context['done_appointments'] = Appointments.objects.filter(status = 'Done').count()

        context['pending_bills'] = AccountStatus.objects.filter(status = 'Pending').count()
        context['done_bills'] = AccountStatus.objects.filter(status = 'Done').count()
        context['total_bills'] = AccountStatus.objects.count()

        earnings = Consultations.objects.aggregate(Sum('price'))
        
        for key, value in earnings.items():
            context['earnings'] = value

        return context