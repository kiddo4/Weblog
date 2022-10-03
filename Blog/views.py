from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import HttpResponse
from .form import CommentForm 
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from django.db.models import Q 
def home(request):
 posts = Post.objects.all()
 context={
 'posts':posts
 }
 return render(request,'home.html', context)
 
class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
        
class SearchResultsView(ListView):
    model = Post
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__contains=query) | Q(Body__contains=query)
        )
        return object_list
# Create your views here.
