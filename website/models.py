from django.db import models
from django.core.validators import MinLengthValidator

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

class Category(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "categories"

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=150)
    eventDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    info = models.TextField()
    createdDate = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="events", null=True)
    toPresent = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    guest_name = models.CharField(max_length=120)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name = "events")