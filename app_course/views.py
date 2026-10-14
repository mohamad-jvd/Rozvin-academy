from django.shortcuts import render
from .models import Course


def index(request):
    courses = Course.objects.select_related("instructor").all()

    return render(request, "index.html", {
        "courses": courses,
    })
