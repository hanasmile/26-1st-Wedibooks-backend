from django.urls import path, include
from .views import ProductView

urlpatterns = [
	path('/detail/<int:id>', ProductView.as_view()),
]