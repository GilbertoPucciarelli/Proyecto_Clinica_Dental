from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from users.models import Profile
from appointments.models import WorkBlocks, Appointments, Consultations
from appointments.forms import WorkBlockForm, AppointmentsForm
from medical_records.models import MedicalRecords, AccountStatus
from medical_records.forms import MedicalRecordForm, AccountStatusForm


# --- MEDICAL RECORDS --- #


class MedicalRecordsFeedView(LoginRequiredMixin, ListView):

    template_name = 'medical_records/feed.html'
    model = MedicalRecords
    context_object_name = 'records'


class CreateMedicalRecordView(LoginRequiredMixin, CreateView):

    template_name = 'medical_records/update.html'
    form_class = MedicalRecordForm
    success_url = reverse_lazy('appointments:feed')

    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id

        return context


class MedicalRecordsDoctorsFeedView(LoginRequiredMixin, ListView):

    template_name = 'medical_records/feed_doctors.html'
    model = MedicalRecords
    context_object_name = 'records'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['consultations'] = Consultations.objects.filter(doctor_id = self.request.user.id)
        context['users'] = User.objects.all()

        return context


# --- CONSULTATIONS --- #


class ConsultationsDoctorFeedView(LoginRequiredMixin, ListView):

    template_name = 'medical_records/consultations_feed.html'
    model = Consultations
    context_object_name = 'consultations'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs['user_id']
        context['doctor_id'] = self.request.user.id
        context['blocks'] = WorkBlocks.objects.all()
        context['bills'] = AccountStatus.objects.all()

        return context


class ConsultationsPacientFeedView(LoginRequiredMixin, ListView):

    template_name = 'medical_records/consultations_feed_pacient.html'
    model = Consultations
    context_object_name = 'consultations'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs['user_id']
        context['blocks'] = WorkBlocks.objects.all()
        context['users'] = User.objects.all()

        return context


# --- ACCOUNT STATUS --- #


class AccountFeedView(LoginRequiredMixin, ListView):

    template_name = 'users/account.html'
    model = AccountStatus
    context_object_name = 'accounts'

    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        context['users'] = User.objects.all()
        context['blocks'] = WorkBlocks.objects.all()
        context['consultations'] = Consultations.objects.all()

        return context


class SendBillView(LoginRequiredMixin, CreateView):

    template_name = 'medical_records/send_bill.html'
    form_class = AccountStatusForm
    success_url = reverse_lazy('appointments:feed_doctors')

    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['consultation'] = Consultations.objects.get(appointment_id = self.kwargs['appointment_id'])
        consultation = Consultations.objects.get(appointment_id = self.kwargs['appointment_id'])
        bills = AccountStatus.objects.all()

        for bill in bills:
            
            if bill.consultation_id == consultation.pk:

                context['record'] = False

        return context