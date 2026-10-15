from django.db import models
from django.utils.text import slugify


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
    skills = models.TextField(
    verbose_name="مهارت‌ها",
    help_text="مهارت‌ها را با کامای انگلیسی (,) جدا کنید. مثال: Python, Linux, Django"
)
    work_experience = models.TextField(verbose_name="سوابق کاری")

    
    email = models.EmailField(
        blank=True,
        verbose_name="ایمیل"
    )

    telegram_url = models.URLField(
        blank=True,
        verbose_name="لینک تلگرام"
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شهر"
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "استادها"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام دسته‌بندی"
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        verbose_name="شناسه دسته‌بندی"
    )

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

    is_popular = models.BooleanField(
        default=False,
        verbose_name="نمایش در دوره‌های پرطرفدار"
    )

    instructor = models.ForeignKey(
        "app_course.Instructor",
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="استاد"
    )

    category_obj = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="courses",
        null=True,
        blank=True,
        verbose_name="دسته‌بندی"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره‌ها"


class CourseTopic(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="topics",
        verbose_name="دوره"
    )
    title = models.CharField(max_length=200, verbose_name="عنوان سرفصل")
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ["order"]
        verbose_name = "سرفصل"
        verbose_name_plural = "سرفصل‌ها"


class SiteBanner(models.Model):
    image = models.ImageField(
        upload_to="banners/",
        verbose_name="تصویر بنر"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="بنر فعال"
    )

    def __str__(self):
        return "بنر سایت"

    class Meta:
        verbose_name = "بنر پایین سایت"
        verbose_name_plural = "بنر پایین سایت"



class SiteSettings(models.Model):
    telegram_url = models.URLField(
        verbose_name="لینک تلگرام ",
        help_text="لینک کامل کانال تلگرام را وارد کنید.",
        default="https://t.me/YourChannel",
    )

    logo = models.ImageField(
        upload_to="site/",
        verbose_name="لوگوی سایت",
        blank=True,
        null=True,
        help_text="تصویر لوگوی سایت را بارگذاری کنید.",
    )


    class Meta:
        verbose_name = "لینک تلگرام "
        verbose_name_plural = "لینک تلگرام و لوگو"

    def __str__(self):
        return "لینک تلگرام"


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


class Education(models.Model):
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="educations",
        verbose_name="رزومه"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="مدرک یا عنوان دوره"
    )
    institution = models.CharField(
        max_length=200,
        verbose_name="دانشگاه یا مؤسسه"
    )
    start_year = models.CharField(
        max_length=10,
        verbose_name="سال شروع"
    )
    end_year = models.CharField(
        max_length=10,
        blank=True,
        verbose_name="سال پایان"
    )
    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "سابقه تحصیلی"
        verbose_name_plural = "سوابق تحصیلی"

    def __str__(self):
        return f"{self.title} - {self.institution}"


class WorkExperience(models.Model):
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="experiences",
        verbose_name="رزومه"
    )
    job_title = models.CharField(
        max_length=200,
        verbose_name="عنوان شغلی"
    )
    company = models.CharField(
        max_length=200,
        verbose_name="نام شرکت یا مجموعه"
    )
    start_year = models.CharField(
        max_length=10,
        verbose_name="سال شروع"
    )
    end_year = models.CharField(
        max_length=10,
        blank=True,
        verbose_name="سال پایان"
    )
    description = models.TextField(
        verbose_name="توضیحات و مسئولیت‌ها"
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "سابقه کاری"
        verbose_name_plural = "سوابق کاری"

    def __str__(self):
        return f"{self.job_title} - {self.company}"


class SiteStatistic(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان آمار")
    value = models.DecimalField(
        max_digits=12,
        decimal_places=1,
        default=0,
        verbose_name="مقدار"
    )
    suffix = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="پسوند (مثلاً + یا ساعت)"
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="ترتیب نمایش"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نمایش در سایت"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "آمار سایت"
        verbose_name_plural = "آمارهای سایت"

    def __str__(self):
        return self.title
