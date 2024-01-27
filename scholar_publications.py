from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_scholar_profiles(teacher_names, driver_path):
    # Initialize the browser driver
    driver = webdriver.Chrome(executable_path=driver_path)

    profiles = []

    for name in teacher_names:
        # Navigate to Google Scholar
        driver.get('https://scholar.google.com/')

        # Find the search box and enter the teacher's name
        search_box = driver.find_element(By.NAME, 'q')
        search_box.clear()
        search_box.send_keys(name)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2) # Wait for page to load

        try:
            # Click on the first profile link
            profile_link = driver.find_element(By.XPATH, '//*[@id="gs_res_ccl_mid"]/div/div/div/h3/a')
            profile_link.click()

            time.sleep(2) # Wait for profile page to load

            # Scrape the titles of the publications
            titles = [title.text for title in driver.find_elements(By.CLASS_NAME, 'gsc_a_at')]

            profiles.append({'Name': name, 'Titles': titles})
        except Exception as e:
            print(f"Error scraping data for {name}: {e}")

    driver.quit()
    return profiles

# Example usage
teacher_names = ['Teacher One', 'Teacher Two']  # Replace with actual names
driver_path = 'path/to/your/chromedriver.exe'  # Update with your driver path

# Scrape the profiles
data = scrape_scholar_profiles(teacher_names, driver_path)

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('scholar_profiles.csv', index=False)
