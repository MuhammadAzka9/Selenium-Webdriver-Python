from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from multiprocessing import Process

chromedriver_autoinstaller.install()

def login_and_close_browser():
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

        time.sleep(5)

    except Exception as e:
        print(f"Assertion Error: {e}")

    finally:
        # Tutup browser
        webdriver_instance.quit()

if __name__ == "__main__":
    # List untuk menyimpan objek Process
    processes = []

    # Membuat dan menjalankan 10 proses
    for _ in range(30):
        process = Process(target=login_and_close_browser)
        processes.append(process)
        process.start()

    # Menunggu semua proses selesai
    for process in processes:
        process.join()
