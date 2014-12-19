import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import LoadAvgSample, LoadAvgEvent
import calendar
from datetime import datetime, timedelta
import socket

def sample_to_object(sample):
    time_in_seconds = calendar.timegm(sample.timestamp.timetuple()) if hasattr(sample.timestamp, 'timetuple') else 0
    ret_object = {'time': time_in_seconds, 'y': sample.one_minute}

    return ret_object

def event_translation(event):
    ret_object = {'type': event.type, 'message': event.message}
    return ret_object


def index(request):
    hostname = socket.gethostname()
    return render_to_response('index.html', {'hostname':hostname})


def samples(request):
    start_time = datetime.utcnow() - timedelta(minutes=10)
    samples = LoadAvgSample.objects.filter(timestamp__gte=start_time).order_by('timestamp')
    data=map(sample_to_object, samples)
    
    return HttpResponse(json.dumps(data), content_type="application/json")

def latest(request):
    latest_sample = LoadAvgSample.objects.latest('timestamp')

    return HttpResponse(json.dumps(sample_to_object(latest_sample)), content_type="application/json")


def events(request):
    loadEvents = LoadAvgEvent.objects.all().order_by('timestamp').reverse()

    events = map(event_translation, loadEvents)

    return HttpResponse(json.dumps(events), content_type='application/json')
