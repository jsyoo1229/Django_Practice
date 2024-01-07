from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view),
    path('<str:topic>', views.news_view),
    path('<int:num1>/<int:num2>', views.add),
    path('int:<num_page>', views.num_page_view)
    
]
