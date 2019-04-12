from django.shortcuts import render

def propositions(request):
    return render(request, 'propozycje/book.html')
