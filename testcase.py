from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

# Navigate to your webpage
driver.get("https://aasmi18.github.io/magicwebsite/")

try:
    # Find the <h1> tag with the text "Magic Website"
    h1_element = driver.find_element(By.XPATH, "//h1[text()='Magic Website']")

    # If the element is found, print a success message
    print("The webpage has an <h1> tag with the text 'Magic Website'")
except NoSuchElementException:
    # If the element is not found, print an error message
    print("Error: The webpage does not have an <h1> tag with the text 'Magic Website'")

# Close the WebDriver
driver.quit()
