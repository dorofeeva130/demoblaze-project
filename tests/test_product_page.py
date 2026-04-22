from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_open_product_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com")
    driver.maximize_window()
    time.sleep(2)

    product = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
    product.click()
    time.sleep(2)

    assert "Samsung galaxy s6" in driver.page_source
    assert "$360" in driver.page_source or "360" in driver.page_source
    assert "Product description" in driver.page_source

    driver.quit()