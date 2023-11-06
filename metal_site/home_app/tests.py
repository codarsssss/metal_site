from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse

from .models import Category


# Create your tests here.
class GetPagesCase(TestCase):
    fixtures = ["home_app_category.json", "home_app_product.json"]

    def test_mainpage(self):
        path = reverse("home_app:home")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "home_app/index.html")

    def test_detailpage(self):
        c = Category.objects.get(slug="balka-dvutavrovaya")
        path = reverse("home_app:category_detail", args=[c.slug])
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "home_app/detail.html")

    def test_aboutpage(self):
        path = reverse("home_app:about")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "home_app/about.html")

    def test_contactspage(self):
        path = reverse("home_app:contacts")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "home_app/contacts.html")
