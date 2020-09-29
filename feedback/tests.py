from django.test import TestCase
from selenium import webdriver
from time import sleep
# from .models import Feedback


class FeedbackTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        # last = Feedback.objects.last()
        # last.delete() не работает

    def test_add_form_success(self):
        self.driver.get("http://localhost:8000")
        sleep(3)

        phone = self.driver.find_element_by_id("id_phone_number")
        phone.send_keys("+996657434445")

        email = self.driver.find_element_by_id("id_email")
        email.send_keys("aaaaa@gmail.com")

        title = self.driver.find_element_by_id("id_title")
        title.send_keys("Тема")

        text = self.driver.find_element_by_id("id_text")
        text.send_keys("Текст")

        self.driver.find_element_by_xpath("//*[contains(text(), 'Отправить')]")
    
    def test_form_max_length(self):
        self.driver.get("http://localhost:8000/product/all/")

        phone_number = self.driver.find_element_by_id("id_phone_number")
        test = "a" * 270
        phone_number.send_keys(test)
        self.assertNotEqual(test, phone_number.get_attribute("value"))

        email = self.driver.find_element_by_id("id_email")
        test = "a" * 270
        email.send_keys(test)
        self.assertNotEqual(test, email.get_attribute("value"))

        title = self.driver.find_element_by_id("id_title")
        test = "a" * 270
        title.send_keys(test)
        self.assertNotEqual(test, title.get_attribute("value"))