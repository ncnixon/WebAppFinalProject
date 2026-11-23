from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import EventForm, RSVPForm


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_create.html"

    def form_valid(self, form):
        form.instance.event_host = self.request.user
        return super().form_valid(form)

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"

class EventDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Event
    template_name = "events/event_detail.html"

    def test_func(self):
        obj = self.get_object()
        if obj.private:
            return obj.event_host == self.request.user
        else:
            return obj.event_host == obj.event_host

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = RSVPForm()
        context["user_rsvp"] = (
            self.object.rsvps.filter(signup_user=self.request.user).first()
        )
        context["attending_rsvps"] = (
            self.object.rsvps
            .filter(signup=True)
            .select_related("signup_user")
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (
            self.object.event_host == request.user
            or self.object.rsvps.filter(signup_user=request.user).exists()
        ):
            return redirect(self.object.get_absolute_url())

        form = RSVPForm(request.POST)

        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = self.object
            rsvp.signup_user = request.user
            rsvp.save()
            return redirect(self.object.get_absolute_url())

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "events/event_delete.html"
    success_url = reverse_lazy("event_list")

    def test_func(self):
        obj = self.get_object()
        return obj.event_host == self.request.user

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.event_host == self.request.user
