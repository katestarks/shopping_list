from typing import Dict
from django.db.models.query import QuerySet
from your_list.models import List_Items

class ItemsController():
    '''Handles functionality relating to shopping list items'''

    item_names_dictionary = {}

    def adds_items_to_dictionary(self, items: 'QuerySet[List_Items]') -> Dict[str, str]:
        if items:
            for item in items:
                item_name = item["item_name"]
                self.item_names_dictionary[item["id"]] = item_name
