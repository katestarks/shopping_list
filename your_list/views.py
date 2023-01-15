from django.shortcuts import render
from .src.CostsController import CostsController


# Home page view which displays shopping list items
def index(request):
    list = {
        "item_1": {"item": "Lotus", "cost": 60_000},
        "item_2": {"item": "Aeropex", "cost": 165},
        "item_3": {"item": "Garmin", "cost": 585},  
        "item_4": {"item": "Ski Lodge", "cost": 1_200_000},
        "item_5": {"item": "New Puppy", "cost": 120}}
    
    costs_controller = CostsController()
    costs_controller.calculate_basket_total(list)
    costs_controller.int_to_number_format_string(costs_controller.basket_total)

    context = {"list": list, "total": costs_controller.number_formatted_string}

    return render(request, 'your_list/index.html', context)
