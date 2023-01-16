from django.shortcuts import render
from .src.CostsController import CostsController
from .src.ItemsController import ItemsController
from .models import List_Items


# Home page view which displays shopping list items
def index(request):
    items_to_display = List_Items.get_active_items()

    items_controller = ItemsController()
    items_controller.adds_items_to_dictionary(items_to_display)
    
    costs_controller = CostsController()
    costs_controller.get_item_costs(items_to_display)
    costs_controller.calculate_basket_total(costs_controller.item_costs)
    costs_controller.int_to_number_format_string(costs_controller.basket_total)

    context = {
        "list": items_controller.item_names_dictionary,
        "total": costs_controller.number_formatted_string}

    return render(request, 'your_list/index.html', context)
