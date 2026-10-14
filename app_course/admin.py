
from django.contrib import admin
from .models import Instructor, Course, CourseTopic, Category


class CourseTopicInline(admin.TabularInline):
    model = CourseTopic
    extra = 1


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name", "skills")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "instructor",
        "duration",
        "category_obj",
        "price",
    )
    search_fields = ("title", "description")
    list_filter = ("category_obj", "instructor")
    fields = (
        "title",
        "description",
        "duration",
        "image",
        "category_obj",
        "price",
        "instructor",
    )
    inlines = [CourseTopicInline]


@admin.register(CourseTopic)
class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title",)
