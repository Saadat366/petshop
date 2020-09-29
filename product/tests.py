from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        products_url = reverse("products")
        c = Client()
        self.response = c.get(products_url)
        self.products = Product.objects.all()
    
    def test_product_open_200_OK(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Все товары")