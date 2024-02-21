from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def add_to_cart():
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

        # Tambahkan waktu tunggu sebelum mencoba menemukan tombol "ADD TO CART"
        add_to_cart_button = WebDriverWait(webdriver_instance, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))
        )

        # Tambahkan barang ke keranjang
        add_to_cart_button.click()

        # Tunggu sebentar untuk memberikan waktu pada animasi tambah ke keranjang
        time.sleep(2)

        # Verifikasi bahwa barang telah ditambahkan ke keranjang
        cart_quantity = webdriver_instance.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_quantity == "1", f"Assertion Error: Jumlah barang di keranjang tidak sesuai, seharusnya 1, tetapi sekarang {cart_quantity}"

        print("Barang berhasil ditambahkan ke keranjang.")

        time.sleep(5)

    except Exception as e:
        print(f"Assertion Error: {e}")

    finally:
        # Tutup browser
        webdriver_instance.quit()

if __name__ == "__main__":
    add_to_cart()
