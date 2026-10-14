from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import (
    Course,
    Category,
    SiteBanner,
    SiteSettings,
    Banner,
    TrendingTopic,
    HeroContent,
    Testimonial,
    Instructor,
    Education,
    WorkExperience,
    SiteStatistic,
)


def index(request):
    courses = Course.objects.select_related(
        "instructor", "category_obj"
    ).prefetch_related("topics")

    categories = Category.objects.all()

    # بنر پایین سایت خودت
    banner = SiteBanner.objects.filter(is_active=True).first()

    # تنظیمات تلگرام خودت
    site_settings = SiteSettings.objects.first()

    # جست‌وجوی دوره‌ها
    search_query = request.GET.get("q", "").strip()

    if search_query:
        search_results = courses.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
        )
    else:
        search_results = courses.none()

    # قابلیت‌های اضافه‌شده توسط دوستت
    hero_banner = Banner.objects.filter(is_active=True).first()

    trending_topics = TrendingTopic.objects.filter(
        is_active=True
    ).order_by("order")

    hero_content = HeroContent.objects.first()
    testimonials = Testimonial.objects.filter(is_active=True)
    instructors = Instructor.objects.all()
    site_statistics = SiteStatistic.objects.filter(
        is_active=True
    )

    return render(request, "index.html", {
        "courses": courses,
        "categories": categories,
        "banner": banner,
        "hero_banner": hero_banner,
        "trending_topics": trending_topics,
        "hero_content": hero_content,
        "testimonials": testimonials,
        "instructors": instructors,
        "site_statistics": site_statistics,
        "search_query": search_query,
        "search_results": search_results,
        "search_performed": bool(search_query),
        "site_settings": site_settings,
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
    ).select_related(
        "instructor", "category_obj"
    ).prefetch_related("topics")

    return render(request, "category_courses.html", {
        "category": category,
        "courses": courses,
    })


def resume_view(request):
    instructor = Instructor.objects.first()

    skills_list = []

    if instructor and instructor.skills:
        skills_list = [
            skill.strip()
            for skill in instructor.skills.replace("،", ",").split(",")
            if skill.strip()
        ]

    educations = (
        Education.objects.filter(instructor=instructor)
        if instructor else Education.objects.none()
    )

    experiences = (
        WorkExperience.objects.filter(instructor=instructor)
        if instructor else WorkExperience.objects.none()
    )

    return render(request, "resume.html", {
        "instructor": instructor,
        "skills_list": skills_list,
        "educations": educations,
        "experiences": experiences,
    })


def instructor_resume_view(request, instructor_id):
    instructor = get_object_or_404(
        Instructor,
        pk=instructor_id
    )

    skills_list = []

    if instructor.skills:
        skills_list = [
            skill.strip()
            for skill in instructor.skills.replace("،", ",").split(",")
            if skill.strip()
        ]

    educations = Education.objects.filter(
        instructor=instructor
    )

    experiences = WorkExperience.objects.filter(
        instructor=instructor
    )

    return render(request, "resume.html", {
        "instructor": instructor,
        "skills_list": skills_list,
        "educations": educations,
        "experiences": experiences,
    })
