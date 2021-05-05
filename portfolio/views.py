from django.shortcuts import render

# Create your views here.

def portfolio(request):
    """ A view to return the portfolio page """

    return render(request, 'home/portfolio.html')
