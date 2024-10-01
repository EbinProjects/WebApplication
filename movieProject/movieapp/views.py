import django.contrib.auth
import django.contrib.auth.models
from django.shortcuts import render, redirect
from .models import MovieTimes, Registration
from .forms import MovieForms
import django.contrib.messages


# Create your views here.
def MyMovie(request):
    movie = MovieTimes.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, 'index.html', context)


def Details(request, movie_id):
    data = MovieTimes.objects.get(id=movie_id)

    return render(request, 'Details.html', {'movie': data})


def AddMovie(request):
    if request.method == "POST":
        name = request.POST.get('movie_name')
        desc = request.POST.get('movie_description')
        year = request.POST.get('movie_number')
        if year == '' or not year.isdigit() or len(year) != 4:
            django.contrib.messages.info(request, "enter valid year!")
            return redirect('movieapp:AddMovie')
        images = request.FILES['movie_image']
        movie = MovieTimes(name=name, desc=desc, year=year, images=images)
        movie.save()

    return render(request, 'add.html')


def Update(request, id):
    movie = MovieTimes.objects.get(id=id)
    form = MovieForms(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form})


def Delete(request, dele_id):
    if request.method == "POST":
        movie = MovieTimes.objects.get(id=dele_id)
        movie.delete()
        return redirect('movieapp:MyMovie')
    return render(request, 'delete.html')


def Registration1(request):
    if request.method == "POST":
        first = request.POST.get('first')
        email = request.POST.get('email')
        last = request.POST.get('end')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password_confirm')

        # Check if passwords match
        if password == confirmPassword:
            # Check if username already exists
            if django.contrib.auth.models.User.objects.filter(username=username).exists():
                django.contrib.messages.info(request, "Username is already taken!")
                return redirect('movieapp:register')
            else:
                # Create new user
                user = django.contrib.auth.models.User.objects.create_user(
                    email=email,
                    first_name=first,
                    last_name=last,
                    username=username,
                    password=password
                )
                user.save()
                return redirect('movieapp:login')
        else:
            django.contrib.messages.info(request, "Passwords do not match!")
            return redirect('movieapp:register')  # Redirect back to registration form
    return render(request, 'register.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = django.contrib.auth.authenticate(username=username, password=password)

        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect('/')
        else:
            django.contrib.messages.info(request, "user not exist!")
            return redirect('movieapp:login')

    return render(request, 'login.html')


def LogOut(request):
    django.contrib.auth.logout(request)
    return redirect('/')
