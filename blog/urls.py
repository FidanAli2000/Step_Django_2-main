from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("posts/", views.post_list, name="posts_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<slug:category_slug>/", views.category_detail, name="category_detail"),
    path("author/<str:name>/", views.author_posts, name="author_posts"),
    path("latest/", views.latest, name="latest"),
    path("stats/", views.stats, name="stats"),
]
