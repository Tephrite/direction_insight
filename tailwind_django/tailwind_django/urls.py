from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("what_we_do/", TemplateView.as_view(template_name="what_we_do.html"), name="what_we_do"),
    path("programs/", TemplateView.as_view(template_name="programs.html"), name="programs"),
    path("reviews/", TemplateView.as_view(template_name="reviews.html"), name="reviews"),
    path("booking/", views.booking, name="booking"),
]
