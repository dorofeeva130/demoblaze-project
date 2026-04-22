from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.demoblaze.com")
        driver.maximize_window()

        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product.click()

        add_to_cart = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart.click()

        alert = wait.until(EC.alert_is_present())
        assert "Product added" in alert.text
        alert.accept()

        cart_button = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
        cart_button.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Samsung galaxy s6')]")))

    finally:
        driver.quit()