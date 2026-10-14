
from django.contrib import admin
from .models import Instructor, Course, CourseTopic, Category, SiteBanner, SiteSettings


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

    def has_module_permission(self, request):
        return super().has_module_permission(request)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("telegram_url",)

    def has_add_permission(self, request):
        # فقط یک رکورد تنظیمات اجازه ساخت دارد
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)