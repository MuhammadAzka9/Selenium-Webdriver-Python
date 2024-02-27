from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

    # Cari dan klik tombol menu burger menggunakan WebDriverWait
    WebDriverWait(webdriver_instance, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='react-burger-menu-btn']"))
    ).click()

    # Cari dan klik tombol logout menggunakan WebDriverWait
    WebDriverWait(webdriver_instance, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']"))
    ).click()

    # Assertion: Memastikan bahwa berhasil logout
    WebDriverWait(webdriver_instance, 10).until(EC.url_matches("https://www.saucedemo.com/"))

    print("Assertion berhasil! Logout berhasil.")

except Exception as e:
    print(f"Assertion Error: {e}")

finally:
    # Tutup browser
    webdriver_instance.quit()
