from django.shortcuts import render, redirect
from .src.CostsController import CostsController
from .src.ItemsController import ItemsController
from .src.AddItemForm import AddItemForm
from .models import List_Items


# Home page view which displays shopping list items
def index(request):
    items_to_display = List_Items.get_active_items()

    items_controller = ItemsController()
    items_controller.add_items_to_display_dictionary(items_to_display)
    
    costs_controller = CostsController()
    costs_controller.get_item_costs(items_to_display)
    costs_controller.calculate_basket_total(costs_controller.item_costs)
    costs_controller.int_to_number_format_string(costs_controller.basket_total)

    context = {
        "list": items_controller.item_names_dictionary,
        "total": costs_controller.number_formatted_string}

    return render(request, 'your_list/index.html', context)

def add_item(request):
    
    if request.method == "POST":
        add_item_form = AddItemForm(request.POST)

        if add_item_form.is_valid():
            items_controller = ItemsController()
            items_controller.item_name=request.POST["item_name"]
            items_controller.item_cost=request.POST["item_cost"]
            items_controller.add_item_to_list_items_db()
        return redirect('index')
    
    else:
        add_item_form = AddItemForm()
        return render(request, "your_list/add_item.html", {"form": add_item_form})
