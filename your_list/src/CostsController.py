from typing import Dict

class CostsController():
    '''Handles calculations relating to shopping list pricing'''

    basket_total = 0
    number_formatted_string = ""

    def calculate_basket_total(self, shopping_list: Dict[str, int]) -> int:
        total = 0
        for k, v in shopping_list.items():
            self.basket_total += v["cost"]
        
    
    def int_to_number_format_string(self, value: int) -> str:
        self.number_formatted_string = "{:,}".format(value)