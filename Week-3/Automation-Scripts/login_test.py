# login_test.py 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = r"D:\SQA_Week3\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    print("✓ Opened SauceDemo")
    
    # Wait for page to load
    time.sleep(3)
    
    # Enter username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")
    print("✓ Entered username")
    time.sleep(1)
    
    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    print("✓ Entered password")
    time.sleep(1)
    
    # Click login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("✓ Clicked login")
    
    # Wait for login
    time.sleep(5)
    
    # Verify login
    if "inventory" in driver.current_url:
        print("✅ TEST PASSED - Login successful!")
        
        # Take screenshot
        driver.save_screenshot("login_success.png")
        print("✓ Screenshot saved as login_success.png")
        
        # Keep browser open for 5 seconds so you can see
        print("✓ Browser will stay open for 5 seconds...")
        time.sleep(5)
    else:
        print("❌ TEST FAILED - Login failed")
        driver.save_screenshot("login_failed.png")
    
finally:
    driver.quit()
    print("✓ Browser closed")
    print("Test completed")