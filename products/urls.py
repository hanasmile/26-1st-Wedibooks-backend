from django.urls import path, include
from .views import ProductView, ProductListView

urlpatterns = [
	path('/<int:id>', ProductView.as_view()),
	path('', ProductListView.as_view()),
]