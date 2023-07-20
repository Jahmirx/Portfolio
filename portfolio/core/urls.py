from django.urls import path
from .views import HomeTemplateView, contact_view


urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('contact/', contact_view, name='contact'),
]