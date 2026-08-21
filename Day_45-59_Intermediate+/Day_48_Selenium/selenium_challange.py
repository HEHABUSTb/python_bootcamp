from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from types import SimpleNamespace

driver = webdriver.Chrome()
driver.get(r"https://www.python.org/")
upcoming_events = driver.find_elements(By.CSS_SELECTOR,".event-widget li")

if not len(upcoming_events) == 5:
    raise AssertionError(f"Expected 5 upcoming events, but got {len(upcoming_events)}")

result = []
for event in upcoming_events:
    time = event.find_element(By.CSS_SELECTOR, "time")
    # print(time.text)

    name = event.find_element(By.CSS_SELECTOR, "a")
    # print(name.text)
    result.append(SimpleNamespace(name=name.text, time=time.text))

pprint(result)