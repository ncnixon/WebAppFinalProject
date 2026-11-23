from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import RSVPForm
from .models import Event, RSVP


class RSVPDetailTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="attendee",
            password="test-password",
        )
        self.host = get_user_model().objects.create_user(
            username="host",
            password="test-password",
        )
        self.event = Event.objects.create(
            title="Django Meetup",
            date_time=timezone.now(),
            location="Library",
            description="A meetup",
            private=False,
            event_host=self.host,
        )

    def test_detail_contains_rsvp_form(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("event_detail", kwargs={"pk": self.event.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], RSVPForm)

    def test_post_creates_rsvp_for_user_and_event(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("event_detail", kwargs={"pk": self.event.pk}),
            {"signup": "Yes"},
        )

        self.assertRedirects(
            response,
            reverse("event_detail", kwargs={"pk": self.event.pk}),
        )
        rsvp = RSVP.objects.get()
        self.assertEqual(rsvp.event, self.event)
        self.assertEqual(rsvp.signup_user, self.user)
        self.assertIs(rsvp.signup, True)

        detail_response = self.client.get(
            reverse("event_detail", kwargs={"pk": self.event.pk})
        )
        self.assertContains(detail_response, "attendee")
        self.assertContains(detail_response, "attendee is going.")
        self.assertNotContains(detail_response, "Are you going?")

    def test_rsvp_list_excludes_false_signups(self):
        RSVP.objects.create(
            event=self.event,
            signup=False,
            signup_user=self.user,
        )
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("event_detail", kwargs={"pk": self.event.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No users have marked themselves as going.")
        self.assertNotContains(response, "attendee is going.")

    def test_host_does_not_see_rsvp_form(self):
        self.client.force_login(self.host)

        response = self.client.get(
            reverse("event_detail", kwargs={"pk": self.event.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Are you going?")

    def test_existing_rsvp_hides_form_even_when_signup_is_false(self):
        RSVP.objects.create(
            event=self.event,
            signup=False,
            signup_user=self.user,
        )
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("event_detail", kwargs={"pk": self.event.pk})
        )

        self.assertNotContains(response, "Are you going?")
