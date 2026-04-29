from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_product_page():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.demoblaze.com")
        driver.maximize_window()

        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".name")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-container")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#more-information")))

        assert "Samsung galaxy s6" in driver.page_source
        assert "$360" in driver.page_source or "360" in driver.page_source
        assert "Product description" in driver.page_source

    finally:
        driver.quit()