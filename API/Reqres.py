import requests

# URL API Reqres
api_url = "https://reqres.in/api/users/2"

def test_get_user(api_url):
    # Kirim permintaan GET ke API
    response = requests.get(api_url)

    # Periksa status code
    assert response.status_code == 200, f"Failed to get user. Status code: {response.status_code}"

    # Parse JSON respons
    user_data = response.json()

    return user_data

def assert_user_data(user_data, expected_id, expected_email):
    # Verifikasi data pengguna
    assert user_data["data"]["id"] == expected_id, f"User ID doesn't match. Expected: {expected_id}, Actual: {user_data['data']['id']}"
    assert user_data["data"]["email"] == expected_email, f"User email doesn't match. Expected: {expected_email}, Actual: {user_data['data']['email']}"

def test_case():
    # Panggil fungsi test_get_user untuk mendapatkan data pengguna
    user_data = test_get_user(api_url)

    # Panggil fungsi assert_user_data untuk memverifikasi data pengguna
    assert_user_data(user_data, expected_id=2, expected_email="janet.weaver@reqres.in")

    print("Test passed successfully. User data:", user_data)

if __name__ == "__main__":
    test_case()
