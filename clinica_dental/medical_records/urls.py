
from django.urls import path
from medical_records import views


urlpatterns = [

    path(
        route = 'medical_records/feed',
        view = views.MedicalRecordsFeedView.as_view(),
        name = 'feed',
    ),

    path(
        route = 'medical_records/create',
        view = views.CreateMedicalRecordView.as_view(),
        name = 'create',
    ),

    path(
        route = 'medical_records/feed_doctors',
        view = views.MedicalRecordsDoctorsFeedView.as_view(),
        name = 'feed_doctors',
    ),

    path(
        route = 'medical_records/consultations_feed/<int:user_id>',
        view = views.ConsultationsDoctorFeedView.as_view(),
        name = 'feed_consultations',
    ),

    path(
        route = 'medical_records/consultations_feed_pacient/<int:user_id>',
        view = views.ConsultationsPacientFeedView.as_view(),
        name = 'feed_pacient',
    ),

    path(
        route = 'medical_records/account',
        view = views.AccountFeedView.as_view(),
        name = 'account',
    ),

    path(
        route = 'medical_records/send_bill/<int:appointment_id>',
        view = views.SendBillView.as_view(),
        name = 'send_bill',
    ),

]