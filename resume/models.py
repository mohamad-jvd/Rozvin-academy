from django.db import models
from app_course.models import Instructor as OriginalInstructor
from app_course.models import Education as OriginalEducation
from app_course.models import WorkExperience as OriginalWorkExperience


class Instructor(OriginalInstructor):
    class Meta:
        proxy = True
        app_label = "resume"
        verbose_name = "استاد"
        verbose_name_plural = "استادها"


class Education(OriginalEducation):
    class Meta:
        proxy = True
        app_label = "resume"
        verbose_name = "سابقه تحصیلی"
        verbose_name_plural = "سوابق تحصیلی"


class WorkExperience(OriginalWorkExperience):
    class Meta:
        proxy = True
        app_label = "resume"
        verbose_name = "سابقه کاری"
        verbose_name_plural = "سوابق کاری"