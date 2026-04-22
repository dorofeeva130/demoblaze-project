from selenium import webdriver
import requests


def test_homepage_status_code():
    response = requests.get("https://www.demoblaze.com")
    assert response.status_code == 200


def test_homepage_loads():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.demoblaze.com")

        assert "STORE" in driver.page_source or "PRODUCT STORE" in driver.page_source

    finally:
        driver.quit()