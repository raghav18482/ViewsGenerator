import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

def create_views():
    driver = webdriver.Chrome()
    url = "https://www.youtube.com/watch?v=nQCciv8-XCk"
    driver.get(url)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']"))).click()
    # Note: No need for time.sleep() here
    driver.quit()

# Define the number of threads/screens you want to open
num_threads = 30

# Create a list to hold the threads
threads = []

# Create and start threads
for _ in range(num_threads):
    thread = threading.Thread(target=create_views)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed.")
