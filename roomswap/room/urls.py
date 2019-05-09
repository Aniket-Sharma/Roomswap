from django.urls import path

from .views import SignUpView, HomePageView, DelView

app_name = 'accounts'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', SignUpView.as_view(), name='register'),
    path('delete/', DelView.as_view(), name='delete'),
]
