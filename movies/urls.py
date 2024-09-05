from xml.etree.ElementInclude import include
from django.urls import path
from backend.movies import admin
from . import views

urlpatterns = [
    path('/admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('movies/', views.movie_list_view, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail_view, name='movie_detail'),
    path('api/movies/', views.MovieListAPIView.as_view(), name='api_movie_list'),
    path('api/movies/<int:pk>/', views.MovieDetailAPIView.as_view(), name='api_movie_detail'),
    path('', views.landing_page_view, name='landing_page'),  # Default landing page
    path('/api/', include('movies.urls'))
]
