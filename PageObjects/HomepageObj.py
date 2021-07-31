from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Homepage:
    searchField = (By.XPATH, "//input[@id='LocationSearch_input']")
    initialSuggestion = (By.XPATH, "//input[@id='LocationSearch_input']")
    listOfSuggestions = (By.XPATH, "//div[@id='LocationSearch_listbox']")
    listOfActiveSuggestions = (By.XPATH, "//div[@id='LocationSearch_listbox']/button")
    symbol = "°"

    def __init__(self, driver):
        self.driver = driver

    def searchCity(self, city):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located(Homepage.searchField))
        wait.until(expected_conditions.element_to_be_clickable(Homepage.searchField))
        self.driver.find_element(*Homepage.searchField).send_keys(city)
        self.driver.find_element(*Homepage.initialSuggestion)
        # wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[contains(@class,'SearchResults--open')]")))
        wait.until(expected_conditions.visibility_of_element_located(Homepage.listOfSuggestions))

        suggestions = self.driver.find_elements(*Homepage.listOfActiveSuggestions)
        print(len(suggestions))

        for suggestion in suggestions:
            print(suggestion.text)
            if suggestion.text == "Delhi":
                suggestion.click()
                break
