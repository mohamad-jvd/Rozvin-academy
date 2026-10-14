
from django.shortcuts import render, get_object_or_404
from .models import (
    Course,
    Category,
    Banner,
    TrendingTopic,
    HeroContent,
    Testimonial,
    Instructor,
    Education,
    WorkExperience,
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
    testimonials = Testimonial.objects.filter(is_active=True)
    instructors = Instructor.objects.all()

    return render(request, "index.html", {
        "courses": courses,
        "categories": categories,
        "banner": banner,
        "trending_topics": trending_topics,
        "hero_content": hero_content,
        "testimonials": testimonials,
        "instructors": instructors,
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
