from django.shortcuts import render

# Create your views here.

def contactme(request):
    """ A view to return the contactme page """

    return render(request, 'home/contactme.html')
