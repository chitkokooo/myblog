from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name="detail")
]