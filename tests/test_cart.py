from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_add_product_to_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com")
    driver.maximize_window()
    time.sleep(2)

    product = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
    product.click()
    time.sleep(2)

    add_to_cart = driver.find_element(By.LINK_TEXT, "Add to cart")
    add_to_cart.click()
    time.sleep(2)

    alert = Alert(driver)
    assert "Product added" in alert.text
    alert.accept()
    time.sleep(1)

    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)

    assert "Samsung galaxy s6" in driver.page_source

    driver.quit()