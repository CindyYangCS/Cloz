from django.shortcuts import render, get_object_or_404
from .models import Garment
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserGarmentListView(ListView):
    model = Garment
    template_name = 'closet/user-garments.html'
    context_object_name = 'garments'
    ordering = ['brand']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Garment.objects.filter(user=user)

class GarmentDetailView(DetailView):
    model = Garment