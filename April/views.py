from bubble.models import *

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

# def index(request):
#     bubbledefinitions = BubbleDefinition.objects.all()[:500]
#     output = '<br/>'.join(['<a href="bubbledefinition/' + str(bt.id) + '">' + bt.label + '</a>' for bt in bubbledefinitions])
#     return HttpResponse(output)

def bubbledefinition(request, bubbledefinition_id):
    # bubbledefinition = BubbleDefinition.objects.get(pk = bubbledefinition_id)
    bubbledefinition = get_object_or_404(BubbleDefinition, pk = bubbledefinition_id)
    bubbles = Bubble.objects.all()[:500]

    return render_to_response('bubble/bubbledefinition.html', {
        'bubbledefinition': bubbledefinition,
        'bubbles': bubbles,
        })

