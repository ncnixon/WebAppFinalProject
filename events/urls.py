from django.urls import path
from .views import (
    EventCreateView,
    EventListView,
    EventDetailView,
    EventDeleteView,
    EventUpdateView,
)

urlpatterns = [
    path("<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("<int:pk>/update/", EventUpdateView.as_view(), name="event_update"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
    path("new/", EventCreateView.as_view(), name="event_create"),
    path("event_list/", EventListView.as_view(), name="event_list"),
]
