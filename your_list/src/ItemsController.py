from typing import Dict
from django.db.models.query import QuerySet
from your_list.models import List_Items


class ItemsController():
    '''Handles functionality relating to displaying shopping list items'''

    item_names_dictionary = {}
    item_name = ""
    item_cost = 0

    def add_items_to_display_dictionary(self, items: 'QuerySet[List_Items]') -> None:
        if items:
            for item in items:
                item_name = item["item_name"]
                self.item_names_dictionary[item["id"]] = item_name
    
    def add_item_to_list_items_db(self) -> None:
        new_item = List_Items(item_name=self.item_name, item_cost=self.item_cost)
        new_item.save()
