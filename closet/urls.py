from django.urls import path
from .views import UserGarmentListView, GarmentDetailView

urlpatterns = [
    path('closet/<str:username>', UserGarmentListView.as_view(), name='user-garments'),
]