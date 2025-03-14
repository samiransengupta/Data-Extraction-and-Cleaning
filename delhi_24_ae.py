from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time

# Initialize WebDriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
website = 'https://results.eci.gov.in/ResultAcGenFeb2025/index.htm'
driver.get(website)
driver.maximize_window()
time.sleep(3)

#CSV file to store results
csv_file = "election_results_all.csv"
if os.path.exists(csv_file):
    existing_data = pd.read_csv(csv_file)
    scraped_options = set(existing_data["Dropdown_Option"].unique())  # Track completed options
else:
    existing_data = pd.DataFrame()
    scraped_options = set()

# Function to get a fresh dropdown reference
def get_dropdown():
    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='card-header']/select[@class='custom-select']")
    ))
    return Select(dropdown_element)

# Get initial dropdown
dropdown = get_dropdown()

# Loop through dropdown options
for i in range(1, len(dropdown.options)):  # Start from 1 to skip the placeholder
    try:
        # Get fresh dropdown reference before selecting
        dropdown = get_dropdown()
        option_name = dropdown.options[i].text  

        if option_name in scraped_options:
            print(f"Skipping '{option_name}', already scraped.")
            continue  

        print(f"Scraping '{option_name}'...")

        dropdown.select_by_index(i)
        time.sleep(3)

        # Click on button to navigate to table
        button_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="switch-list"]//li[3]//a')
        ))
        button_2.click()
        time.sleep(3)

        # Locate table
        table_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='custom-table']//table[@class='table table-striped table-bordered']")
        ))

        # Convert table to DataFrame
        table_html = table_element.get_attribute('outerHTML')
        df = pd.read_html(table_html)[0]
        df["Dropdown_Option"] = option_name  

        # Append to CSV safely
        df.to_csv(csv_file, mode='a', index=False, header=not os.path.exists(csv_file))
        scraped_options.add(option_name)  # Mark as scraped
        print(f"Saved '{option_name}' successfully!")

    except Exception as e:
        print(f"Error on '{option_name}': {e}. Retrying after refresh...")
        driver.get(website)  # Reload the website
        time.sleep(5)

#Close browser
driver.quit()
