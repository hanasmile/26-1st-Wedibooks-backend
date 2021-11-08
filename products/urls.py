from django.urls import path, include
from .views import ProductView, ProductListView

urlpatterns = [
	path('/<int:id>', ProductView.as_view()),
    path("/briefproducts", ProductListView.as_view()),
	path("/briefproducts/<int:sub_category>", ProductListView.as_view()),
]