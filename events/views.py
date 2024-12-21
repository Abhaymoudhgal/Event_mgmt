from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Attendee, Task
from .forms import EventForm, AttendeeForm, TaskForm
from django.contrib.auth.forms import UserCreationForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'events/attendee_list.html', {'attendees': attendees})

def attendee_create(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendee_list')
    else:
        form = AttendeeForm()
    return render(request, 'events/attendee_form.html', {'form': form})

def attendee_edit(request, id):
    attendee = get_object_or_404(Attendee, id=id)
    if request.method == 'POST':
        form = AttendeeForm(request.POST, instance=attendee)
        if form.is_valid():
            form.save()
            return redirect('attendee_list')
    else:
        form = AttendeeForm(instance=attendee)
    return render(request, 'events/attendee_form.html', {'form': form, 'attendee': attendee})

def attendee_delete(request, id):
    attendee = get_object_or_404(Attendee, id=id)
    if request.method == 'POST':
        attendee.delete()
        return redirect('attendee_list')  # Redirect to the attendee list after deletion
    return render(request, 'events/attendee_confirm_delete.html', {'attendee': attendee})

def task_list(request, event_id):
    event = Event.objects.get(id=event_id)
    tasks = Task.objects.filter(event=event)
    return render(request, 'events/task_list.html', {'event': event, 'tasks': tasks})

def task_create(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.event = event
            task.save()
            return redirect('task_list', event_id=event.id)
    else:
        form = TaskForm()
    return render(request, 'events/task_form.html', {'form': form, 'event': event})