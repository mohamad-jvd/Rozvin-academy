from django.contrib import admin
from .models import (
    Instructor,
    Course,
    CourseTopic,
    Category,
    SiteBanner,
    SiteSettings,
    Banner,
    TrendingTopic,
    HeroContent,
    Testimonial,
    SiteStatistic,
)


class CourseTopicInline(admin.TabularInline):
    model = CourseTopic
    extra = 1


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
        "is_popular",
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
        "is_popular",
        "instructor",
    )
    inlines = [CourseTopicInline]


@admin.register(CourseTopic)
class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title",)


@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active")
    list_filter = ("is_active",)



@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("telegram_url", "logo", "favicon")
    fields = ("telegram_url", "logo", "favicon")

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)



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


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("name", "role", "content")
    ordering = ("order",)


@admin.register(SiteStatistic)
class SiteStatisticAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "suffix", "order", "is_active")
    list_editable = ("value", "suffix", "order", "is_active")
    search_fields = ("title",)
    list_filter = ("is_active",)
    ordering = ("order",)
