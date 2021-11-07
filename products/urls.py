from django.urls import path, include
from .views import ProductView

urlpatterns = [
	path('/<int:id>', ProductView.as_view()),
]