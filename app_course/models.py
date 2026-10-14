from django.db import models


class Instructor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    photo = models.ImageField(
        upload_to="instructors/",
        blank=True,
        null=True,
        verbose_name="عکس استاد"
    )
    biography = models.TextField(verbose_name="بیوگرافی")
    skills = models.TextField(verbose_name="مهارت‌ها")
    work_experience = models.TextField(verbose_name="سوابق کاری")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "استادها"

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name="شناسه دسته‌بندی")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

class Course(models.Model):

    title = models.CharField(max_length=200, verbose_name="نام دوره")
    description = models.TextField(verbose_name="توضیحات دوره")
    duration = models.CharField(max_length=100, verbose_name="مدت زمان دوره")

    image = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True,
        verbose_name="عکس دوره"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="قیمت دوره"
    )

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="استاد"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره‌ها"

    category_obj = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="courses",
        null=True,
        blank=True,
        verbose_name="دسته‌بندی"
    )



class CourseTopic(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="topics",
        verbose_name="دوره"
    )
    title = models.CharField(max_length=200, verbose_name="عنوان سرفصل")
    order = models.PositiveIntegerField(default=1, verbose_name="ترتیب نمایش")

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ["order"]
        verbose_name = "سرفصل"
        verbose_name_plural = "سرفصل‌ها"



class Banner(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="عنوان بنر"
    )
    image = models.ImageField(
        upload_to="banners/",
        verbose_name="تصویر بنر"
    )
    link = models.URLField(
        blank=True,
        verbose_name="لینک مقصد"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    def __str__(self):
        return self.title or f"بنر {self.pk}"

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنرها"




class TrendingTopic(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="عنوان موضوع"
    )
    link = models.URLField(
        blank=True,
        verbose_name="لینک مقصد"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
        verbose_name = "موضوع ترند"
        verbose_name_plural = "موضوعات ترند"




class HeroContent(models.Model):
    eyebrow = models.CharField(
        max_length=250,
        verbose_name="متن بالای عنوان"
    )
    title = models.CharField(
        max_length=250,
        verbose_name="عنوان اصلی"
    )
    description = models.TextField(
        verbose_name="توضیحات زیر عنوان"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محتوای بنر اصلی"
        verbose_name_plural = "محتوای بنر اصلی"




class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام کاربر")
    role = models.CharField(
        max_length=150,
        verbose_name="عنوان یا شغل کاربر"
    )
    content = models.TextField(verbose_name="متن تجربه کاربر")
    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True,
        verbose_name="عکس کاربر"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نمایش در سایت"
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order"]
        verbose_name = "نظر کاربر"
        verbose_name_plural = "نظرات کاربران"