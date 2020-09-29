from django.test import TestCase, Client
from django.urls import reverse
from selenium import webdriver
# class HomepageTestCase(TestCase):
#     def test_open_hp_200_OK(self):
#         c = Client()
#         response = c.get("/") # follow=True
#         self.assertEqual(response.status_code, 200)

# вернет AssertionError потому что домашняя страница redirect на products в views
# а redirect это код 302
# поэтому -->

class HomepageTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get("/")

    # def tearDown(self):

    def test_redirect_hp_302_success(self):
        # responce = c.get("/") # follow=True
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response.url, reverse("products")) # не поломается при смене эндпоинта
    
    def test_open_homepage_200_fail(self):
        self.assertNotEqual(self.response.status_code, 200)


class AuthTestCase(TestCase):
    def test_load_auth_page_success(self):
        driver = webdriver.Chrome()
        driver.get("localhoost:8000")
        driver.find_element_by_xpath("//a[@href='/login/']").click()
        # driver.find_element_by_xpath("//a[contains(@href, 'login')]").click()
        assert "form" in driver.page_source()
        # self.assertIn("form", driver.page_source)