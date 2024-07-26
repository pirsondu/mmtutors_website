from django.db import models

# Create your models here.
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