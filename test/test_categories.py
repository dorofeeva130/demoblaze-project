from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_categories_switch():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com")
    driver.maximize_window()
    time.sleep(2)

    phones = driver.find_element(By.LINK_TEXT, "Phones")
    phones.click()
    time.sleep(2)
    assert "Samsung galaxy s6" in driver.page_source or "Nokia lumia 1520" in driver.page_source

    laptops = driver.find_element(By.LINK_TEXT, "Laptops")
    laptops.click()
    time.sleep(2)
    assert "Sony vaio i5" in driver.page_source or "MacBook air" in driver.page_source

    monitors = driver.find_element(By.LINK_TEXT, "Monitors")
    monitors.click()
    time.sleep(2)
    assert "Apple monitor 24" in driver.page_source or "ASUS Full HD" in driver.page_source

    driver.quit()