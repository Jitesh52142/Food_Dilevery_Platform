
from fastapi import FastAPI
from app.routers import auth_router, user_router, restaurant_router, cart_router, order_router, payment_router

app = FastAPI(title="Food Delivery Platform")

app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(restaurant_router.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(cart_router.router, prefix="/cart", tags=["Cart"])
app.include_router(order_router.router, prefix="/orders", tags=["Orders"])
app.include_router(payment_router.router, prefix="/payments", tags=["Payments"])
