from django.shortcuts import render
from app1.models import Emp
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.

class EmpListView(ListView):
    model = Emp

class EmpDetailView(DetailView):
    model = Emp

class EmpCreateView(CreateView):
    model = Emp
    fields = ('name','location','ceo')

class EmpUpdateView(UpdateView):
    model = Emp
    fields = ('name','ceo')

class EmpDeleteView(DeleteView):
    model = Emp
    success_url = reverse_lazy('employees')





