from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import base_url, random_chars_and_numbers_string
import allure




class TestLoginPageLogin:
    """5. When I enter correct combination of username and password, I would be redirected to my dashboard screen."""
    def test_neg_login_wrong_email(self):
        pass

    def test_neg_login_wrong_password(self):
        pass

    def test_neg_login_wrong_emailandpassword(self):
        pass

    def test_pos_login(self):
        pass