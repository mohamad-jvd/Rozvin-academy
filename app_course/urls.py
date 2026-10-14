from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
    path("category/<slug:slug>/", views.category_courses, name="category_courses"),
    path("resume/", views.resume_view, name="resume"),
    path(
    "instructor/<int:instructor_id>/",
    views.instructor_resume_view,
    name="instructor_resume",
),
]
