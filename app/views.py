from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from app.models import *

# Create your views here.

class LandingPageView(View):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        techFest = TechFest.objects.all()
        events = Events.objects.all()
        speakers = Speakers.objects.all()
        sponsors = Sponsors.objects.all()
        return render(request, template_name="index.html", context={'techFest': techFest,'events':events,'speakers':speakers,'sponsors':sponsors})

class AboutUsView(View):
    template_name = 'about-us.html'

    def get(self, request, **kwargs):
        techFest = TechFest.objects.all()
        return render(request, template_name="about-us.html", context={'techFest': techFest})


class StudentCouncilView(View):
    template_name = 'student-council.html'

    def get(self, request, **kwargs):
        studentCouncil = StudentCouncilMembers.objects.filter(is_design_team=False).order_by('created_at')
        designTeam= StudentCouncilMembers.objects.filter(is_design_team=True).order_by('created_at')
        return render(request, template_name="student-council.html", context={'studentCouncil' : studentCouncil,'designTeam' : designTeam})
    
class ContactView(View):
    template_name = 'contact.html'

    def get(self, request, **kwargs):
        techFest = TechFest.objects.all()
        return render(request, template_name="contact.html", context={'techFest': techFest})

class EventsView(View):
    template_name = 'events.html'

    def get(self, request, **kwargs):
        events = Events.objects.all()
        return render(request, template_name="events.html", context={'events':events})

class EventView(View):
    template_name = 'event.html'

    def get(self, request, **kwargs):
        event = Events.objects.get(id=kwargs['event_id'])
        studentCoordinators= StudentCoordinators.objects.filter(event= event.id)
        teacherCoordinators= TeacherCoordinators.objects.filter(event= event.id)
        return render(request, template_name="event.html", context={'event':event,'studentCoordinators':studentCoordinators,'teacherCoordinators':teacherCoordinators})


class EventsTimelineView(View):
    template_name = 'event-timeline.html'

    def get(self, request, **kwargs):
        eventTimeline = EventsTimeLine.objects.all()
        return render(request, template_name="event-timeline.html", context={'eventTimeline':eventTimeline})