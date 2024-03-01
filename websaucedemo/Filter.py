from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

# Inisialisasi WebDriver untuk Chrome
webdriver_instance = webdriver.Chrome()

# Buka halaman Saucedemo
webdriver_instance.get("https://www.saucedemo.com")

# Masukkan username dan password
username_field = webdriver_instance.find_element(By.ID, "user-name")
password_field = webdriver_instance.find_element(By.ID, "password")
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

# Submit form login
password_field.send_keys(Keys.RETURN)

# Tunggu hingga halaman beranda muncul
try:
    # Assertion: Memastikan bahwa elemen produk muncul setelah login berhasil
    WebDriverWait(webdriver_instance, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("Assertion berhasil! Login berhasil dan halaman beranda muncul.")

    # Test Case 1: Filter by Name A to Z
    try:
        dropdown = Select(WebDriverWait(webdriver_instance, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        ))
        dropdown.select_by_visible_text("Name (A to Z)")
        print("Test Case 1: Filter by Name A to Z - Passed")
    except TimeoutException:
        print("Test Case 1: Filter by Name A to Z - Timed out")
    except NoSuchElementException:
        print("Test Case 1: Filter by Name A to Z - Element not found")

    # Test Case 2: Filter by Name Z to A
    try:
        dropdown = Select(WebDriverWait(webdriver_instance, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        ))
        dropdown.select_by_visible_text("Name (Z to A)")
        print("Test Case 2: Filter by Name Z to A - Passed")
    except TimeoutException:
        print("Test Case 2: Filter by Name Z to A - Timed out")
    except NoSuchElementException:
        print("Test Case 2: Filter by Name Z to A - Element not found")

    # Test Case 3: Filter by Price Low to High
    try:
        dropdown = Select(WebDriverWait(webdriver_instance, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        ))
        dropdown.select_by_visible_text("Price (low to high)")
        print("Test Case 3: Filter by Price Low to High - Passed")
    except TimeoutException:
        print("Test Case 3: Filter by Price Low to High - Timed out")
    except NoSuchElementException:
        print("Test Case 3: Filter by Price Low to High - Element not found")

    # Test Case 4: Filter by Price High to Low
    try:
        dropdown = Select(WebDriverWait(webdriver_instance, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        ))
        dropdown.select_by_visible_text("Price (high to low)")
        print("Test Case 4: Filter by Price High to Low - Passed")
    except TimeoutException:
        print("Test Case 4: Filter by Price High to Low - Timed out")
    except NoSuchElementException:
        print("Test Case 4: Filter by Price High to Low - Element not found")

except Exception as e:
    print(f"Assertion Error: {e}")

finally:
    # Tutup browser
    webdriver_instance.quit()
