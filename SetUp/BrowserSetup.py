from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def browser_setup(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome() # Or Firefox(), Edge(), etc.
    elif browser_name == "firefox":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser {browser_name} is not valid")

    return driver

def handle_dropdown(webdriver):
    dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
    dropdown_element.click()
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option2")
    dropdown.select_by_value("option1")
    dropdown.select_by_index(2)

def handle_alerts(webdriver):
    driver.find_element(By.ID, "alertbtn").click()
    alart = driver.switch_to.alert
    alart.accept()

def switch_frame(webdriver):
    chaild_frame = driver.switch_to.frame("courses-iframe")
    text1 = driver.find_element(By.XPATH, "//ul[@class='clearfix']/li").text
    driver.switch_to.default_content()
    text = driver.find_element(By.XPATH, "//div[@class='block large-row-spacer']/fieldset/legend").text

def switch_tabs(webdriver):
    parent_window = driver.current_window_handle
    title1 = driver.title
    driver.find_element(By.ID, "opentab").click()
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[1])
    title2 = driver.title

driver = browser_setup("chrome")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.quit()
