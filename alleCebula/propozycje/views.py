from django.shortcuts import render
from machineLearning.rules import create_rules, get_associated_categories


def propositions(request):
    return render(request, 'propozycje/book.html')

def process(request):
    #get data from API and machine learning stuff
    category="monitory"
    rules = create_rules()
    associated_items = get_associated_categories(rules, category)

    items_number = 100
    category_number = len(associated_items)
    items_per_category = items_number // category_number


    return render(request, 'propozycje/book.html')
