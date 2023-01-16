from django.test import TestCase
from django.urls import reverse

from .src.CostsController import CostsController
from .src.ItemsController import ItemsController
from .models import List_Items

# In the display tests, test_url_available_by_name checks URL identifier
# This is a Django framework pattern which enables us to use the built-in
# reverse() method in further tests.
# reverse() uses the name of the route to get the URL, meaning the tests
# still work if the URL changes


class HomepageTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/your_list/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "your_list/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Shopping List")


class CostControllerTests(TestCase):

    def test_basket_totaller_integer_addition(self):
        costs_controller = CostsController()
        test_values = {"item_1": 2, "item_2": 2}
        costs_controller.calculate_basket_total(test_values)
        self.assertEquals(costs_controller.basket_total, 4)
        self.assertIsInstance(costs_controller.basket_total, int)

    def test_string_number_converstion_formats_correctly(self):
        costs_controller = CostsController()
        costs_controller.basket_total = 50000
        costs_controller.int_to_number_format_string(costs_controller.basket_total)
        self.assertEquals(costs_controller.number_formatted_string, "50,000")
        self.assertNotEquals(costs_controller.number_formatted_string, "50000")
        self.assertIsInstance(costs_controller.number_formatted_string, str)


class AddItemDisplayTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/your_list/addItem")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("addItem"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("addItem"))
        self.assertTemplateUsed(response, "your_list/add_item.html")

    def test_template_content(self):
        response = self.client.get(reverse("addItem"))
        self.assertContains(response, "Add an item!")


class ListItemsModelTests(TestCase):

    def setUp(self):
        List_Items.objects.create(item_name="milk", item_cost=1.2, item_deleted=True)
        List_Items.objects.create(item_name="bread", item_cost=1.7)

    # Checking both items are in the db to confirm deleted filter function tested below
    def test_get_all_items(self):
        items = List_Items.objects.all()
        length_of_items_list = len(items)
        self.assertEqual(length_of_items_list, 2)
    
    def test_get_items_not_deleted(self):
        items = List_Items.get_active_items()
        length_of_items_list = len(items)
        self.assertEqual(length_of_items_list, 1)


class ItemController(TestCase):
    def setUp(self):
        List_Items.objects.create(item_name="milk", item_cost=1.2)
        List_Items.objects.create(item_name="bread", item_cost=1.7)

    # Checking both items are in the db to confirm add item function tested below
    def test_get_all_items(self):
        items = List_Items.objects.all()
        length_of_items_list = len(items)
        self.assertEqual(length_of_items_list, 2)

    def test_add_item_to_list_items_db(self):
        items_controller = ItemsController()
        items_controller.item_name="cheese"
        items_controller.item_cost=4.5
        items_controller.add_item_to_list_items_db()
        items = List_Items.objects.all()
        length_of_items_list = len(items)
        self.assertEqual(length_of_items_list, 3)
