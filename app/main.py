from fastapi import FastAPI
from app.routers import auth_router, restaurant_router, cart_router, order_router, payment_router
from app.routers import menu_router
from app.routers import review_router, delivery_router



app = FastAPI(title="Food Delivery Platform")

app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(restaurant_router.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(cart_router.router, prefix="/cart", tags=["Cart"])
app.include_router(order_router.router, prefix="/orders", tags=["Orders"])
app.include_router(payment_router.router, prefix="/payments", tags=["Payments"])
app.include_router(review_router.router, prefix="/reviews", tags=["Reviews"])
app.include_router(delivery_router.router, prefix="/delivery", tags=["Delivery"])
app.include_router(menu_router.router, prefix="/menu", tags=["Menu"])


