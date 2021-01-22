from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from users.models import Profile
from appointments.models import WorkBlocks, Appointments
from appointments.forms import WorkBlockForm, AppointmentsForm, EditAppointmentsForm, ConsultationsForm
from .models import WorkBlocks
from medical_records.models import MedicalRecords


# --- APPOINTMENTS --- #


class AppointmentsHomeView(LoginRequiredMixin, ListView):

    template_name = 'appointments/home.html'
    model = Profile
    context_object_name = 'usuarios'


class AppointmentsFeedView(LoginRequiredMixin, ListView):

    template_name = 'appointments/feed.html'
    model = Appointments
    context_object_name = 'appointments'

    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['blocks'] = WorkBlocks.objects.all()
        context['records'] = MedicalRecords.objects.filter(user_id=self.request.user.id)

        if not context['records']:
            context['record'] = True # No existe el medical record de este paciente

        return context


class AppointmentsFeedDoctorView(LoginRequiredMixin, ListView):

    template_name = 'appointments/feed_doctor.html'
    model = Appointments
    context_object_name = 'appointments'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['blocks'] = WorkBlocks.objects.filter(doctor_id=self.request.user.id)
        context['users'] = User.objects.all()

        return context


class AddAppointmentsPreview(LoginRequiredMixin, ListView):

    template_name = 'appointments/add_preview.html'
    model = WorkBlocks
    context_object_name = 'blocks'


class AddAppointmentsView(LoginRequiredMixin, CreateView):

    template_name = 'appointments/add.html'
    form_class = AppointmentsForm
    success_url = reverse_lazy('appointments:feed')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        context['appointments'] = Appointments.objects.filter(block_id = self.kwargs['block_id'])
        
        if not context['appointments']:
            context['appointment'] = True  # Esta vacío 

        context['block_id'] = self.kwargs['block_id']

        return context

    
class DeleteAppointmentsView(LoginRequiredMixin, DeleteView):

    model = Appointments
    template_name = 'appointments/delete.html'
    success_url = reverse_lazy('appointments:feed')


class UpdateAppointmentsView(LoginRequiredMixin, UpdateView):

    template_name = 'appointments/update.html'
    model = Appointments
    form_class = EditAppointmentsForm
    success_url = reverse_lazy('appointments:feed_doctors')


# --- WORK BLOCKS --- #


class WorkBlocksView(LoginRequiredMixin, ListView):

    template_name = 'work_blocks/feed.html'
    model = WorkBlocks
    context_object_name = 'blocks'


class AddWorkBlocksView(LoginRequiredMixin, CreateView):

    template_name = 'work_blocks/add.html'
    form_class = WorkBlockForm
    success_url = reverse_lazy('appointments:work_blocks')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['doctor_id'] = self.request.user.id
        context['doctor_name'] = self.request.user.get_full_name

        return context

    
class DeleteWorkBlocksView(LoginRequiredMixin, DeleteView):

    model = WorkBlocks
    template_name = 'work_blocks/delete.html'
    success_url = reverse_lazy('appointments:work_blocks')


# --- CONSULTATIONS --- #


class AddConsultationsView(LoginRequiredMixin, CreateView):

    template_name = 'consultations/add.html'
    form_class = ConsultationsForm
    success_url = reverse_lazy('appointments:feed_doctors')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['data'] = Appointments.objects.get(pk = self.kwargs['appointment_id'])
        context['doctor_id'] = self.request.user.id
        context['appointment_id'] = self.kwargs['appointment_id']

        return context

    
    def form_valid(self, form, **kwargs):

        response = super(AddConsultationsView, self).form_valid(form)
        query = Appointments.objects.filter(pk = self.kwargs['appointment_id'])
        query.update(status='Done')

        return response