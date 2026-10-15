from django.contrib import admin
from .models import Instructor, Education, WorkExperience



@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "city",
        "email",
    )

    search_fields = (
        "first_name",
        "last_name",
        "skills",
        "email",
        "city",
    )

    fields = (
        "first_name",
        "last_name",
        "photo",
        "biography",
        "skills",
        "work_experience",
        "city",
        "email",
        "telegram_url",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "title", "institution", "instructor",
        "start_year", "end_year", "order"
    )
    list_filter = ("instructor",)
    search_fields = ("title", "institution")
    ordering = ("order",)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "job_title", "company", "instructor",
        "start_year", "end_year", "order"
    )
    list_filter = ("instructor",)
    search_fields = ("job_title", "company")
    ordering = ("order",)