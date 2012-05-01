from bubble.models import *

from django.http import HttpResponse

def index(request):
    bubbletypes = BubbleDefinition.objects.all()[:500]
    output = '<br/>'.join(['<a href="bubbletype/' + str(bt.id) + '">' + bt.label + '</a>' for bt in bubbletypes])
    return HttpResponse(output)

def bubbletype(request, bubbletype_id):
    bubbletype = BubbleDefinition.objects.get(pk = bubbletype_id)
    output = '<a href="bubbletype/' + str(bubbletype.id) + '">' + bubbletype.label + '</a>'
    return HttpResponse(output)

