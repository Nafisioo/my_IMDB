from django.contrib.auth import authenticate, login, logout # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django import forms # type: ignore
from django.shortcuts import get_object_or_404 # type: ignore
from .models import Movie
from rest_framework import generics # type: ignore
from .serializers import MovieSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''

    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('landing_page')  # Redirect to the login page after logging out

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('landing_page')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def landing_page_view(request):
    return render(request, 'landing_page.html')

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies' : movies})

def movie_detail_view(request, movie_id):
    movies = get_object_or_404('Movie', id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def landing_page_view(request):
    return render(request, 'landing_page.html')

# API View for Movie List
class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# API View for Movie Detail
class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer