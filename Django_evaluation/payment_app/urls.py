from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserView.as_view(), name="users"),
    path("user/detail/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    path("services/", views.ServiceView.as_view(), name="services"),
    path("service/detail/<int:pk>", views.ServiceDetail.as_view(), name="service_detail"),
    path("subscriptions/", views.SubscriptionView.as_view(), name="subsciption"),
    path("create/subscription/", views.Create_sub.as_view(), name="create_subsciption"),
]