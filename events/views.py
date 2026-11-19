from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "events/event_create.html"
    fields = ("title", "date_time", "location", "description")

    def form_valid(self, form):
        form.instance.event_host = self.request.user
        return super().form_valid(form)

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "events/event_detail.html"

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "events/event_delete.html"
    success_url = reverse_lazy("event_list")

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = "events/event_edit.html"
    fields = (
        "title",
        "date_time",
        "location",
        "description",
    )
