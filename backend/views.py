from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import PostForm
from .forms import LoginForm
from .models import User
from .models import Post


def home(request):
    title = "Start a post"
    form = PostForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        context = {
            "title": "Posted"
        }
    return render(request, "home.html", context)


def login(request):
    title = "Enter your credentials"
    form = LoginForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        result = User.objects.filter(username=username)
        if result and password == result[0].password:
            return redirect("success_show", user_id=result[0].user_id)
        else:
            title="Password and username do not match! Enter again"
            context = {
                "title": title,
                "form": form,
            }

    return render(request, "login.html", context)


def success_show(request, user_id):
    message = ["You are successfully logged in!", "The posts made by you are:"]
    context = {
                "title": message[0],
                "message": message[1],
    }

    result = Post.objects.filter(user_id=user_id)
    print(result[0].content)
    if result:
        context["post"] = result[0].content

    return render(request, "success_show.html", context)
