import requests
import json

BASE_URL = "http://localhost:8000"

results = []

def log_result(name, response):
    if response.status_code in [200, 201]:
        print(f"✅ {name} - PASSED")
        results.append((name, "PASSED"))
    else:
        print(f"❌ {name} - FAILED ({response.status_code})")
        print(response.text)
        results.append((name, "FAILED"))

# -----------------------------
# AUTH
# -----------------------------

print("\n🔐 AUTH TESTS")

register_data = {
    "email": "testuser@example.com",
    "password": "test123"
}

r = requests.post(f"{BASE_URL}/auth/register", json=register_data)
log_result("Register", r)

r = requests.post(f"{BASE_URL}/auth/login", json=register_data)
log_result("Login", r)

token = r.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

r = requests.get(f"{BASE_URL}/auth/me", headers=headers)
log_result("Get Me", r)

# -----------------------------
# RESTAURANT
# -----------------------------

print("\n🍴 RESTAURANT TESTS")

restaurant_data = {
    "name": "Test Restaurant",
    "location": "Mumbai",
    "cuisine": "Indian"
}

r = requests.post(f"{BASE_URL}/restaurants/", json=restaurant_data, headers=headers)
log_result("Create Restaurant", r)
restaurant_id = r.json().get("id")

r = requests.get(f"{BASE_URL}/restaurants/")
log_result("List Restaurants", r)

r = requests.get(f"{BASE_URL}/restaurants/{restaurant_id}")
log_result("Get Restaurant By ID", r)

# -----------------------------
# MENU
# -----------------------------

print("\n🍔 MENU TESTS")

menu_data = {
    "name": "Burger",
    "price": 150,
    "restaurant_id": restaurant_id
}

r = requests.post(f"{BASE_URL}/menu/", json=menu_data)
log_result("Create Menu Item", r)
menu_id = r.json().get("id")

r = requests.get(f"{BASE_URL}/menu/{restaurant_id}")
log_result("Get Menu", r)

# -----------------------------
# CART
# -----------------------------

print("\n🛒 CART TESTS")

cart_data = {
    "menu_item_id": menu_id,
    "quantity": 2
}

r = requests.post(f"{BASE_URL}/cart/add", json=cart_data, headers=headers)
log_result("Add To Cart", r)

r = requests.get(f"{BASE_URL}/cart/", headers=headers)
log_result("Get Cart", r)

# -----------------------------
# ORDER
# -----------------------------

print("\n📦 ORDER TESTS")

r = requests.post(f"{BASE_URL}/orders/", headers=headers)
log_result("Create Order", r)
order_id = r.json().get("order_id")

r = requests.get(f"{BASE_URL}/orders/", headers=headers)
log_result("Get Orders", r)

r = requests.get(f"{BASE_URL}/orders/{order_id}", headers=headers)
log_result("Get Order By ID", r)

# -----------------------------
# PAYMENT
# -----------------------------

print("\n💳 PAYMENT TESTS")

payment_data = {
    "order_id": order_id,
    "payment_method": "card"
}

r = requests.post(f"{BASE_URL}/payments/process?order_id={order_id}", headers=headers)
log_result("Process Payment", r)

# -----------------------------
# REVIEW
# -----------------------------

print("\n⭐ REVIEW TESTS")

review_data = {
    "restaurant_id": restaurant_id,
    "rating": 5,
    "comment": "Great food!"
}

r = requests.post(f"{BASE_URL}/reviews/", json=review_data, headers=headers)
log_result("Create Review", r)

r = requests.get(f"{BASE_URL}/reviews/{restaurant_id}")
log_result("Get Reviews", r)

# -----------------------------
# DELIVERY
# -----------------------------

print("\n🚚 DELIVERY TESTS")

delivery_data = {
    "order_id": order_id,
    "status": "assigned"
}

r = requests.post(f"{BASE_URL}/delivery/", json=delivery_data, headers=headers)
log_result("Create Delivery", r)

r = requests.get(f"{BASE_URL}/delivery/{order_id}")
log_result("Track Delivery", r)

# -----------------------------
# SUMMARY
# -----------------------------

print("\n📊 FINAL SUMMARY")
passed = sum(1 for _, result in results if result == "PASSED")
failed = sum(1 for _, result in results if result == "FAILED")

print(f"Total Passed: {passed}")
print(f"Total Failed: {failed}")
