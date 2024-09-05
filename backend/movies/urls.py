from xml.etree.ElementInclude import include
from django.urls import path, admin # type: ignore
from .views import MovieListCreate, MovieDetail, ActorListCreate,ActorDetail, RoleListCreate, RoleDetail, ReviewListCreate, ReviewDetail
from backend.movies import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('actors/', ActorListCreate.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorDetail.as_view(), name='actor-detail'),
    path('roles/', RoleListCreate.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleDetail.as_view(), name='role-detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]