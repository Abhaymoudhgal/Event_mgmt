from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    attendees = models.ManyToManyField('Attendee', blank=True)

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    assigned_attendee = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name