from django.test import TestCase
from django.urls import reverse

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
        self.assertNotContains(response, "Your shopping is done")