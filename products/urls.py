from django.urls import path, include
from .views import ProductDetailView

urlpatterns = [
	path('/detail/<int:id>', ProductDetailView.as_view()),
]