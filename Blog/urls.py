from django.urls import path
from Blog.views import home
from .views import PostDetailView,SearchResultsView
urlpatterns = [
    path('', home, name='home'),
    path('search/posts/<slug:slug>/', PostDetailView.as_view(),),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]