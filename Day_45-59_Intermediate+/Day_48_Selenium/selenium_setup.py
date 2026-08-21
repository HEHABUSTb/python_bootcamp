from selenium import webdriver

# Keep Chrome browser open after program finishes
crome_options = webdriver.ChromeOptions()
crome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=crome_options)
driver.get("https://google.com")

# driver.close() // close single active tab
# driver.quit() // quit entire browser
