from django.http import Http404
from django.shortcuts import render

from .data import CATEGORIES, POSTS


def post_list(request):
    return render(request, "posts.html", {"posts": POSTS})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def post_detail(request, post_id):
    for post in POSTS:
        if post["id"] == post_id:
            return render(request, "post_detail.html", {"post": post})
    raise Http404("Post tapılmadı")


def category_list(request):
    return render(request, "categories.html", {"categories": CATEGORIES})


def category_detail(request, category_slug):
    selected_category = None
    category_posts = []

    for category in CATEGORIES:
        if category["slug"] == category_slug:
            selected_category = category
            break

    if selected_category is None:
        raise Http404("Kateqoriya tapılmadı")

    for post in POSTS:
        if post["category"] == category_slug:
            category_posts.append(post)

    context = {
        "category": selected_category,
        "posts": category_posts,
    }
    return render(request, "category_detail.html", context)


def author_posts(request, name):
    posts = []
    for post in POSTS:
        if post["author"] == name:
            posts.append(post)

    return render(request, "author_posts.html", {"author": name, "posts": posts})


def latest(request):
    return render(request, "latest.html", {"posts": POSTS[-3:]})


def stats(request):
    return render(
        request,
        "stats.html",
        {
            "posts": POSTS,
            "categories": CATEGORIES,
        },
    )
