from django.http import HttpResponse, Http404

from django.shortcuts import get_object_or_404, render

from .models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list,}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    response = "You're looking at the results of poll %s."
    return HttpResponse(response % poll_id)

def question(request, poll_id):
    return HttpResponse("You're voting on question %s." % poll_id)