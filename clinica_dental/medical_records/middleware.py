
from django.shortcuts import redirect
from django.urls import reverse


class MedicalRecordCompletionMiddleware():

    def __init__(self, get_response):
        
        self.get_response = get_response


    def __call__(self, request):

        if not request.user.is_anonymous:

            if not request.user.is_staff:
                
                record = request.user.medical_records
                
                if not record.dni or not record.age or not record.birthday or not record.marital_status or not record.nacionality or not record.address:

                    if request.path not in [reverse('medical_records:update'), reverse('users:logout')]:
                        return redirect('medical_records:update')

        response = self.get_response(request)
        return response
