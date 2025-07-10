from django.shortcuts import render, get_object_or_404
from .models import Garment
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_filters.views import FilterView
from .filters import GarmentFilter

# Create your views here.
class UserGarmentListView(LoginRequiredMixin, FilterView):
    model = Garment
    template_name = 'closet/user_garments.html'
    context_object_name = 'garments'
    filterset_class = GarmentFilter

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Garment.objects.filter(user=user)

class GarmentCreateView(LoginRequiredMixin, CreateView):
    model = Garment
    fields = ['type', 'brand', 'name', 'photo', 'date_purchased', 'thrifted']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GarmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Garment
    fields = ['type', 'brand', 'name', 'photo', 'date_purchased', 'thrifted']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        garment = self.get_object()
        if self.request.user == garment.user:
            return True
        return False
    
class GarmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Garment
    def get_success_url(self):
        return reverse('user-garments', kwargs={'username': self.object.user.username})

    def test_func(self):
        garment = self.get_object()
        if self.request.user == garment.user:
            return True
        return False