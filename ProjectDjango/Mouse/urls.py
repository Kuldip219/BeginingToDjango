from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_mouse, name='all_home'),
    path('<int:mice_id>/', views.mouse_detail, name='mouse_detail'), 
    path('info/', views.mouse_info, name='mouse_info'),
]