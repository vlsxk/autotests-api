import httpx

body = {
  "email": "user@example.com",
  "password": "string"
}

login_response=httpx.post("http://localhost:8000/api/v1/authentication/login", json=body)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]
print("access_token:", access_token)
print("Status Code:", login_response.status_code)
users_me_response=httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
users_me_response_data = users_me_response.json()
print("My user info:", users_me_response_data)
print("Status Code:", users_me_response.status_code)