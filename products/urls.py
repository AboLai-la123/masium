from django.urls import path
from . import views

app_name = "Products"

urlpatterns = [
    path("<product_id>", views.product, name="product"),
    path("edit/<product_id>", views.editProduct, name="editProduct"),
]