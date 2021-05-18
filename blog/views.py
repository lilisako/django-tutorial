from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.http import Http404
from django.views.generic import DetailView, ListView

# Create your views here.
class PostListView(ListView):
  model = Post
  template_name = "post_list.html"
  context_object_name = "posts"

class PostDetailView(DetailView):
  model = Post
  pk_url_kwarg = "post_id"
  template_name = "post_detail.html"
  context_object_name = "post"