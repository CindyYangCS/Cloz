from django.urls import path
from .views import UserGarmentListView, GarmentCreateView, GarmentDeleteView, GarmentUpdateView

urlpatterns = [
    path('closet/new/', GarmentCreateView.as_view(), name='garment-create'),
    path('closet/<str:username>/', UserGarmentListView.as_view(), name='user-garments'),
    path('closet/<int:pk>/update', GarmentUpdateView.as_view(), name='garment-update'),
    path('closet/<int:pk>/delete', GarmentDeleteView.as_view(), name='garment-delete'),
]