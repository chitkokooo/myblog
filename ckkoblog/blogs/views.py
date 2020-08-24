from django.shortcuts import render
from django.views import generic
from .models import Blog


class BlogListView(generic.ListView):
	queryset = Blog.objects.filter(is_published=True).order_by('-created_time')
	context_object_name = "blogs"
	template_name = 'blogs/home.html'
	paginate_by = 2


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = 'blogs/detail.html'