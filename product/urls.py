from django.urls import path
from product.views import *

urlpatterns = [
    path("all/", products, name="products"),
    path("category/<int:pk>/", category, name="category"),
    path("category-create/", category_create, name="category-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("product-create/", ProductCreateView.as_view(), name="product-create"),
    path("create-few/", product_create_few, name="product-create-few"),
    path("edit/<int:id>/", product_edit, name="product-edit"),
    path("add-to-cart/<int:id>", add_to_cart, name="add-to-cart"),
]