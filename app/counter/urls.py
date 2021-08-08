from django.urls import path
from .views import CounterView


urlpatterns = [
    path('', CounterView.as_view()),
]