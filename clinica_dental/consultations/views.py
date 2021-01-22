from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from users.models import Profile
from appointments.models import WorkBlocks, Appointments
from appointments.forms import WorkBlockForm, AppointmentsForm, EditAppointmentsForm
from medical_records.models import MedicalRecords


