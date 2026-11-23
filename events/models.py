from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    private = models.BooleanField(default=False)
    event_host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

class RSVP(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="rsvps",
    )
    signup = models.BooleanField(default=False)
    signup_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.signup)

    def get_absolute_url(self):
        return reverse("event_list")
