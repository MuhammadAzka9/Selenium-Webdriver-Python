from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

# Inisialisasi WebDriver untuk Chrome
webdriver = webdriver.Chrome()

# Buka halaman Saucedemo
webdriver.get("https://www.saucedemo.com")

# Masukkan username dan password
username_field = webdriver.find_element(By.ID, "user-name")
password_field = webdriver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")


# Submit form login
password_field.send_keys(Keys.RETURN)

# Tunggu hingga halaman beranda muncul
try:
    # Assertion: Memastikan bahwa pesan kesalahan muncul setelah login gagal
    error_message = WebDriverWait(webdriver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Epic sadface: Username is required']"))
    )
    print("Assertion berhasil! Pesan kesalahan muncul: ", error_message.text)

    time.sleep(5)
    
except Exception as e:
    print(f"Assertion Error: {e}")
finally:
    # Tutup browser
    webdriver.quit()
