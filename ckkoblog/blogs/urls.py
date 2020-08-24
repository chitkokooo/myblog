from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views
from .sitemaps import BlogSitemap


app_name = "blog"

sitemaps = {
	"blogs": BlogSitemap,
}

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name="detail"),
    path('sitemap.xml', sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
