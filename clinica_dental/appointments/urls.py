
from django.urls import path
from appointments import views


urlpatterns = [

    path(
        route = '',
        view = views.AppointmentsHomeView.as_view(),
        name = "home",
    ),

    path(
        route = 'appointments/work_blocks',
        view = views.WorkBlocksView.as_view(),
        name = "work_blocks",
    ),

    path(
        route = 'appointments/add_work_blocks',
        view = views.AddWorkBlocksView.as_view(),
        name = "add_work_blocks",
    ),

    path(
        route = 'appointments/delete_work_blocks/<int:pk>',
        view = views.DeleteWorkBlocksView.as_view(),
        name = "delete_work_blocks",
    ),

    path(
        route = 'appointments/feed',
        view = views.AppointmentsFeedView.as_view(),
        name = "feed",
    ),

    path(
        route = 'appointments/add_preview',
        view = views.AddAppointmentsPreview.as_view(),
        name = "add_preview",
    ),

    path(
        route = 'appointments/add_appointment/<int:block_id>',
        view = views.AddAppointmentsView.as_view(),
        name = "add_appointments",
    ),

    path(
        route = 'appointments/delete_appointment/<int:pk>',
        view = views.DeleteAppointmentsView.as_view(),
        name = "delete_appointments",
    ),

    path(
        route = 'appointments/feed_doctors',
        view = views.AppointmentsFeedDoctorView.as_view(),
        name = "feed_doctors",
    ),

    path(
        route = 'appointments/update_appointment/<int:pk>',
        view = views.UpdateAppointmentsView.as_view(),
        name = "update_appointments",
    ),

    path(
        route = 'consultations/add/<int:appointment_id>',
        view = views.AddConsultationsView.as_view(),
        name = "add_consultations",
    ),

]