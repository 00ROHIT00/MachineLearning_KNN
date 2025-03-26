from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_page, name='input_page'),  # Display the HTML form
    path('predict/', views.predict_genre, name='predict_genre'),  # Handle predictions
]
