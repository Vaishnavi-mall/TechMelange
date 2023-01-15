from django.contrib import admin
from django.urls import path
from app.views import *
from app  import views

urlpatterns = [
    path("",LandingPageView.as_view(), name="home"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("events/", EventsView.as_view(), name="events"),
    path("eventTimeline/", EventsTimelineView.as_view(), name="event-timeline"),
    path("event/event_id=<event_id>/", EventView.as_view(), name="event"),
    path("student-council/", StudentCouncilView.as_view(), name="student-council"),
    path("contact/", ContactView.as_view(), name="contact")


    
]