from selenium.webdriver.common.by import By

UNLOCKED_PRODUCTS = (By.CSS_SELECTOR, ".product.unlocked.enabled")
print(type(UNLOCKED_PRODUCTS))