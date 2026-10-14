from django.shortcuts import render
from .models import Course, Banner, TrendingTopic, HeroContent


def index(request):
    courses = Course.objects.select_related("instructor").all()
    banner = Banner.objects.filter(is_active=True).first()

    trending_topics = TrendingTopic.objects.filter(
        is_active=True
    ).order_by("order")

    hero_content = HeroContent.objects.first()

    return render(request, "index.html", {
        "courses": courses,
        "banner": banner,
        "trending_topics": trending_topics,
        "hero_content": hero_content,
    })
