
from django import forms

from medical_records.models import MedicalRecords, AccountStatus


class MedicalRecordForm(forms.ModelForm):

    class Meta():

        model = MedicalRecords
        fields = ('dni', 'age', 'birthday', 'marital_status', 'nacionality', 'address', 'user')


class AccountStatusForm(forms.ModelForm):

    class Meta():

        model = AccountStatus
        fields = ('status', 'user', 'consultation')