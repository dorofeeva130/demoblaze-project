from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


def test_homepage_status_code():
    response = requests.get("https://www.demoblaze.com")
    assert response.status_code == 200


def test_homepage_loads():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com")

    assert "STORE" in driver.page_source or "PRODUCT STORE" in driver.page_source

    driver.quit()