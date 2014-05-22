from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Poll, Choice
# from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from django.core.urlresolvers import reverse





def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]

    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list,
    # })
    # return HttpResponse(template.render(context))

    context = {'latest_poll_list': latest_poll_list }
    return render(request, 'polls/index.html', context)



    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)

    #return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})

    # return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/result.html', {'poll': poll})

    # result = ', '.join(choice.votes.__str__() for choice in p.choice_set.all() )
    # return HttpResponse(result)
    # return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    # return HttpResponse("You're voting on poll %s." % poll_id)
