from django.shortcuts import render
from .models import Course, Category


def index(request):
    courses = Course.objects.select_related(
        "instructor", "category_obj"
    ).prefetch_related("topics").all()

    categories = Category.objects.all()

    return render(request, "index.html", {
        "courses": courses,
        "categories": categories,
    })
