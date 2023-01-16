from typing import Dict
from django.db.models.query import QuerySet
from your_list.models import List_Items

class CostsController():
    '''Handles functionality relating to shopping list pricing'''

    basket_total = 0
    number_formatted_string = ""
    item_costs = {}

    def calculate_basket_total(self, shopping_list: Dict[str, int]) -> int:
        for k, v in shopping_list.items():
            self.basket_total += v
        
    
    def int_to_number_format_string(self, value: int) -> str:
        self.number_formatted_string = "{:,}".format(value)


    def get_item_costs(self, items: 'QuerySet[List_Items]') -> Dict[str, float]:
        if items:
            for item in items:
                item_cost = item["item_cost"]
                self.item_costs[item["id"]] = item_cost
