from django.contrib import admin
from .models import Instructor, Course, CourseTopic, Banner, TrendingTopic, HeroContent


class CourseTopicInline(admin.TabularInline):
    model = CourseTopic
    extra = 1


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name", "skills")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "duration")
    search_fields = ("title", "description")
    list_filter = ("instructor",)
    inlines = [CourseTopicInline]


@admin.register(CourseTopic)
class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title",)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)




@admin.register(TrendingTopic)
class TrendingTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("order",)



@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    list_display = ("title",)

