from multiprocessing import context
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostsForm, SubmitForm
from . models import posts, submit
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    form = SubmitForm()
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'home.html', {'form': form})


def display(request):
    register = submit.objects.all()
    return render(request, 'display.html', {'register': register})


def update(request, id):
    modify = submit.objects.get(id=id)
    form = SubmitForm(request.POST or None, instance=modify)
    if form.is_valid():
        form.save()
        return redirect('display')
    return render(request, 'home.html', {'form': form, 'modify': modify})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        try:
            user_exists = User.objects.get(username=request.POST['username'])
            messages.success(request, "Username Already Exists")
            user_exists = User.objects.get(email=request.POST['email'])
            messages.success(request, "Email Already Exists")

        except User.DoesNotExist:
            if password == cpassword:
                myuser = User.objects.create_user(
                    username=username, email=email, password=cpassword)
                myuser.firstname = first_name
                myuser.lastname = last_name
                myuser.save()

                login(request, myuser)
                return redirect('default')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged In')
            return redirect('default')

    return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('default')


def default(request):
    fetch = posts.objects.all()
    webseries = fetch.filter(category="WebSeries").count()
    bollywood = fetch.filter(category="Bollywood Movie").count()
    hollywood = fetch.filter(category="Hollywood Movie").count()
    animated = fetch.filter(category="Animated Movie").count()

    context = {"fetch": fetch,"webseries": webseries,"bollywood": bollywood,"hollywood": hollywood,"animated": animated}

    return render(request, 'sets.html', context)

def default_card(request):
        
    return render(request,'sets.html')

@login_required(login_url='signin')
def post(request):
    context = {}
    if request.method == "POST":
        try:
            posts.objects.create(
                full_name=request.POST.get("full_name"),
                category=request.POST.get("category"),
                season=request.POST.get("season"),
                stream_duration=request.POST.get("stream_duration"),
                episodes=request.POST.get("episodes"),
                mode_category=request.POST.get("mode_category"),
                streaming_platform=request.POST.get("streaming_platform"),
                author=request.user
            )
            return redirect("default")
        except:
            context["message"] = "*Invalid details"
    return render(request, 'posts.html', context)


@login_required(login_url="login")
def drop(request, pk):
    post = posts.objects.get(id=pk)
    if request.user == post.author:
        post.delete()
    else:
        return HttpResponse("403 FORBIDDEN")
    return redirect("default")


@login_required(login_url="login")
def modify(request, pk):
    context = {}
    update = posts.objects.get(id=pk)
    if request.method == "POST":
        try:
            posts.objects.update(
                full_name=request.POST.get("full_name"),
                category=request.POST.get("category"),
                season=request.POST.get("season"),
                stream_duration=request.POST.get("stream_duration"),
                episodes=request.POST.get("episodes"),
                mode_category=request.POST.get("mode_category"),
                streaming_platform=request.POST.get("streaming_platform"),
                author=request.user
            )
        except:
            context["message"] = "*Invalid details"
    return render(request, 'posts.html')
    
