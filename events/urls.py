from django.urls import path
from .views import event_list, event_create, attendee_list, attendee_create, task_list, task_create,attendee_edit,attendee_delete


urlpatterns = [
    path('events/', event_list, name='event_list'),
    path('events/create/', event_create, name='event_create'),
    path('attendees/', attendee_list, name='attendee_list'),
    path('attendees/create/', attendee_create, name='attendee_create'),
    path('attendees/edit/<int:id>/', attendee_edit, name='attendee_edit'),
    path('attendees/delete/<int:id>/', attendee_delete, name='attendee_delete'),
    path('events/<int:event_id>/tasks/', task_list, name='task_list'),
    path('events/<int:event_id>/tasks/create/', task_create, name='task_create'),
]