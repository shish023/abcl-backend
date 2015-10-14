from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PostForm, LoginForm, RegisterForm, CommentForm

from .models import User, Post, Comment, Support

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

    #return HttpResponse('Posted')

def login(request):

    form = LoginForm(request.POST or None)

    context = {
        "title": "Log In:",
        "form": form
    }

    if form.is_valid():

        form_username = form.cleaned_data.get("username")
        form_password = form.cleaned_data.get("password")

        valid_user = User.objects.filter(username=form_username)

        if valid_user:

            if form_password == valid_user[0].password:

                context = {
                    "title": "Log In Successful"
                }

                return redirect("/"+valid_user[0].username+"/front/")

            else:

                context = {
                    "title": "The entered password is incorrect"
                }

        else:

            print "here in else"

            context = {
                "title": "User does not exist",
                "link": "Register here"

            }

    return render(request, "login.html", context)

def register(request):

    form =  RegisterForm(request.POST or None)

    context = {
        "title": "Register",
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        context = {
            "title": "Successful",
            "link": "Login to begin"
        }

    return render(request, "register.html", context)

def front(request,user):

    form = PostForm(request.POST or None)

    support_clicked = request.GET.get('form_support_btn')
    unsupport_clicked = request.GET.get('form_unsupport_btn')
    post_id_clicked = request.GET.get('form_post_id')

    print post_id_clicked
    print support_clicked

    user_data = User.objects.get(username=user)

    if support_clicked:
        post_data = Post.objects.get(post_id=int(post_id_clicked))

        support = Support(post_id=post_data,user_id=user_data)
        support.save()

    elif unsupport_clicked:

        support = Support.objects.get(post_id=post_id_clicked,user_id=user_data.user_id)
        support.delete()

    user_support = Support.objects.filter(user_id=user_data.user_id)

    u_id = User.objects.filter(username=user)

    support_list = { instance.post_id.post_id for instance in user_support}

    posts = Post.objects.all()

    context = {
        "user": user,
        "posts": posts,
        "support": support_list,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user_id = user_data
        instance.save()

    return render(request, "front.html", context)

def post(request,user,post):

    form = CommentForm(request.POST or None)

    post_data = Post.objects.get(post_id=post)

    comments = Comment.objects.filter(post_id=post_data.post_id)

    user_data = User.objects.get(username=user)

    context = {
        "user": user,
        "post": post_data,
        "comments": comments,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user_id = user_data
        instance.post_id = post_data
        instance.save()

    return render(request, "post.html", context)