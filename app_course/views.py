from django.shortcuts import render
from django.db.models import Q
from .models import Course, Category, SiteBanner, SiteSettings


def index(request):
    courses = Course.objects.select_related(
        "instructor", "category_obj"
    ).prefetch_related("topics")

    categories = Category.objects.all()

    banner = SiteBanner.objects.filter(is_active=True).first()
    site_settings = SiteSettings.objects.first()

    search_query = request.GET.get("q", "").strip()

    if search_query:
        search_results = courses.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
        )
    else:
        search_results = courses.none()

    return render(request, "index.html", {
        "courses": courses,
        "categories": categories,
        "banner": banner,
        "search_query": search_query,
        "search_results": search_results,
        "search_performed": bool(search_query),
        "site_settings": site_settings,
    })
