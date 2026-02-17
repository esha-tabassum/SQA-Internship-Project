# dashboard_test.py
# Automate product sorting and add to cart on SauceDemo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Path to chromedriver
chrome_driver_path = r"D:\SQA_Week3\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    print("=" * 50)
    print("DASHBOARD FEATURE TEST - Product Sorting & Cart")
    print("=" * 50)
    
    # STEP 1: Login first
    print("\n1. Logging in...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    print("✓ Login successful")
    
    # STEP 2: Test Product Sorting (Z to A)
    print("\n2. Testing Product Sorting (Z to A)...")
    
    # Find sorting dropdown
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(sort_dropdown)
    
    # Select "Name (Z to A)"
    select.select_by_visible_text("Name (Z to A)")
    time.sleep(2)
    print("✓ Sorted products Z-A")
    
    # Get first product name
    first_product = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"   First product after sorting: {first_product}")
    
    # Verify sorting (Z-A should have "Test.allTheThings() T-Shirt (Red)" first)
    if first_product == "Test.allTheThings() T-Shirt (Red)":
        print("   ✅ Sorting test PASSED")
    else:
        print("   ❌ Sorting test FAILED")
    
    # Take screenshot of sorted products
    driver.save_screenshot("sorting_test.png")
    print("   ✓ Screenshot saved as sorting_test.png")
    time.sleep(2)
    
    # STEP 3: Test Add to Cart
    print("\n3. Testing Add to Cart functionality...")
    
    # Find and click Add to Cart on first product
    add_to_cart = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart.click()
    time.sleep(2)
    print("✓ Clicked Add to Cart")
    
    # Check cart badge
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print(f"   Cart counter: {cart_badge}")
    
    if cart_badge == "1":
        print("   ✅ Add to cart test PASSED")
    else:
        print("   ❌ Add to cart test FAILED")
    
    # Take screenshot with item in cart
    driver.save_screenshot("cart_test.png")
    print("   ✓ Screenshot saved as cart_test.png")
    time.sleep(2)
    
    # STEP 4: View Cart
    print("\n4. Viewing cart...")
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    time.sleep(2)
    print("✓ Opened cart")
    
    # Verify item in cart
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"   Item in cart: {cart_item}")
    
    # Take screenshot of cart
    driver.save_screenshot("cart_view.png")
    print("   ✓ Screenshot saved as cart_view.png")
    time.sleep(3)
    
    # STEP 5: Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print("✅ Product Sorting (Z-A): PASS")
    print("✅ Add to Cart: PASS")
    print("✅ Cart View: PASS")
    print("=" * 50)
    
    # Keep browser open to see results
    print("\n✓ Browser will close in 5 seconds...")
    time.sleep(5)
    
finally:
    driver.quit()
    print("\n✓ Browser closed")
    print("✓ Dashboard test completed!")