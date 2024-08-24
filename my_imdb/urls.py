from django.contrib import admin
from django.urls import path
from movies.views import (
    login_view,
    home_view,
    logout_view,
    register_view,
    movie_list_view,
    movie_detail_view,
    landing_page_view,
    MovieListAPIView,
    MovieDetailAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view, name='landing_page'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('movies/', movie_list_view, name='movie_list'),
    path('movies/<int:movie_id>/', movie_detail_view, name='movie_detail'),
    path('api/movies/', MovieListAPIView.as_view(), name='api_movie_list'),  # API endpoint for movie list
    path('api/movies/<int:pk>/', MovieDetailAPIView.as_view(), name='api_movie_detail'),  # API endpoint for movie detail
    path('logout/', logout_view, name='logout'),
]