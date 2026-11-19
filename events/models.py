from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    event_host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

