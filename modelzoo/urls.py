from django.urls import path
from . import views

app_name = 'modelzoo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('nb/<slug:slug>/', views.DetailView_nb.as_view(), name='detail_nb'),
    path('api/hello/', views.hello, name='hello'),
]
