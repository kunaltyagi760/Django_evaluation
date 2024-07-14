from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Service, Subscription, ServiceUser
from .forms import SubscriptionForm
from django.urls import reverse_lazy

class UserView(ListView):
    template_name = 'payment/users.html'
    model = ServiceUser
    context_object_name = 'users'
    
class UserDetail(DetailView):
    template_name = 'payment/user_detail.html'
    model = ServiceUser
    context_object_name = 'user'


class ServiceView(ListView):
    template_name = 'payment/services.html'
    model = Service
    context_object_name = 'services'

class ServiceDetail(DetailView):
    template_name = 'payment/service_detail.html'
    model = Service
    context_object_name = 'service'

class SubscriptionView(ListView):
    template_name = 'payment/subscription.html'
    model = Subscription
    context_object_name = 'subs'

class Create_sub(CreateView):
    template_name = 'payment/create_subscription.html'
    form_class = SubscriptionForm
    success_url = reverse_lazy("subsciption")
