from django.shortcuts import render

def propositions(request):
    return render(request, 'propozycje/book.html')

def process(request):
    #get data from API and machine learning stuff

    return render(request, 'propozycje/book.html')
