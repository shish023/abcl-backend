from django.shortcuts import render

from .forms import PostForm

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