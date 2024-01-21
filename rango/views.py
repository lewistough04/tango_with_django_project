from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
def index(request):
    # Construct a dictionary to pass to the templates engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier
    # Not that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
