
from django.shortcuts import render, get_object_or_404
from .models import (
    Course,
    Category,
    Banner,
    TrendingTopic,
    HeroContent,
)


def index(request):
    courses = Course.objects.select_related(
        "instructor", "category_obj"
    ).prefetch_related("topics").all()

    categories = Category.objects.all()

    banner = Banner.objects.filter(is_active=True).first()

    trending_topics = TrendingTopic.objects.filter(
        is_active=True
    ).order_by("order")

    hero_content = HeroContent.objects.first()

    return render(request, "index.html", {
        "courses": courses,
        "categories": categories,
        "banner": banner,
        "trending_topics": trending_topics,
        "hero_content": hero_content,
    })


def course_detail(request, course_id):
    course = get_object_or_404(
        Course.objects.select_related(
            "instructor", "category_obj"
        ).prefetch_related("topics"),
        pk=course_id,
    )

    return render(request, "course_detail.html", {
        "course": course,
    })


def category_courses(request, slug):
    category = get_object_or_404(Category, slug=slug)

    courses = Course.objects.filter(
        category_obj=category
    ).select_related("instructor", "category_obj").prefetch_related("topics")

    return render(request, "category_courses.html", {
        "category": category,
        "courses": courses,
    })
