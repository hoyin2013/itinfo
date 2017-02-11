from django.shortcuts import render, render_to_response
from issues.models import System, Person, Event


def person_list(request):
    person_lists = Person.objects.all()
    return render_to_response('issue/person_list.html', locals())


def system_list(request):
    system_lists = System.objects.all()
    return render_to_response('issue/system_list.html', locals())


def event_list(request):
    event_lists = Event.objects.all()
    return render_to_response('issue/event_list.html', locals())
