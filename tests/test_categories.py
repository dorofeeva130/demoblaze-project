from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_categories_switch():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.demoblaze.com")
        driver.maximize_window()

        phones = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        phones.click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6")))

        laptops = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
        laptops.click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sony vaio i5")))

        monitors = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Monitors")))
        monitors.click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Apple monitor 24")))

    finally:
        driver.quit()