from django.db import models

class HomeImage(models.Model):
    image = models.ImageField(null=True, blank=True)


class Parent_Question(models.Model):
    question_mm = models.TextField()
    answer_mm = models.TextField()
    question_en = models.TextField()
    answer_en = models.TextField()

    def __str__(self):
        return self.question_mm

    class Meta:
        verbose_name = "Parent Question"
        verbose_name_plural = "Parent Questions"

class Tutor_Question(models.Model):
    question_mm = models.TextField()
    answer_mm = models.TextField()
    question_en = models.TextField()
    answer_en = models.TextField()

    def __str__(self):
        return self.question_mm

    class Meta:
        verbose_name = "Tutor Question"
        verbose_name_plural = "Tutor Questions"

class Achievement(models.Model):
    title = models.TextField()
    subtitle = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    review = models.TextField()

    def __str__(self):
        return self.name