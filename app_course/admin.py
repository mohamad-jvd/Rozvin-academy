
from django.contrib import admin
from .models import Course, CourseTopic, Banner, Category, TrendingTopic, HeroContent, Testimonial


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






