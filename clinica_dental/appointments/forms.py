
from django import forms

from appointments.models import WorkBlocks, Appointments, Consultations

class WorkBlockForm(forms.ModelForm):

    class Meta():
        
        model = WorkBlocks
        fields = ('doctor', 'doctor_name', 'hour', 'day')


class AppointmentsForm(forms.ModelForm):

    class Meta():

        model = Appointments
        fields = ('status', 'user', 'block')


class EditAppointmentsForm(forms.ModelForm):

    class Meta():

        model = Appointments
        fields = ('status',)

    
class ConsultationsForm(forms.ModelForm):

    class Meta():

        model = Consultations
        fields = ('doctor', 'block', 'user', 'appointment', 'symtoms', 'treatment', 'medicaments', 'price', 'payment')
