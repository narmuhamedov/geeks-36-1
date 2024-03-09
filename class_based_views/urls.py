from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListApiView.as_view()),
    path('reviews/<int:id>/', views.ReviewUpdateDeleteApiView.as_view()),
    path('register/', views.RegisterApiView.as_view()),
]
