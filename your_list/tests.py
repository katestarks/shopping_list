from django.test import TestCase
from django.urls import reverse

from .src.CostsController import CostsController

class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/your_list/")
        self.assertEqual(response.status_code, 200)

    # Checks URL identifier - this is a Django framework pattern
    # The provided reverse method uses the name to get the URL
    # This makes the tests more robust, so we can use it now we know it works
    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "your_list/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Shopping List")
        self.assertContains(response, "Total")
        self.assertNotContains(response, "Your shopping is done")


class CostControllerTests(TestCase):
    def test_basket_totaller_integer_addition(self):
        costs_controller = CostsController()
        test_values = {
            "item_1": {"item": "item", "cost": 2},
            "item_2": {"item": "item", "cost": 2},
            "item_3": {"item": "item", "cost": 2},
            "item_4": {"item": "item", "cost": 2},
            "item_5": {"item": "item", "cost": 2}}
        costs_controller.calculate_basket_total(test_values)
        self.assertEquals(costs_controller.basket_total, 10)
        self.assertIsInstance(costs_controller.basket_total, int)

    def test_string_number_converstion_formats_correctly(self):
        costs_controller = CostsController()
        costs_controller.basket_total = 50000
        costs_controller.int_to_number_format_string(costs_controller.basket_total)
        self.assertEquals(costs_controller.number_formatted_string, "50,000")
        self.assertNotEquals(costs_controller.number_formatted_string, "50000")
        self.assertIsInstance(costs_controller.number_formatted_string, str)
