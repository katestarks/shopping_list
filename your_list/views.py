from django.shortcuts import render


# Home page view which displays shopping list items
def index(request):
    list = {
        "item_1": "Lotus",
        "item_2": "Aeropex",
        "item_3": "Garmin",
        "item_4": "Ski Lodge",
        "item_5": "New Puppy"}
    return render(request, 'your_list/index.html', {"list": list})