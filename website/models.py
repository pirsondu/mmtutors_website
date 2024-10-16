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
    image = models.ImageField(upload_to="images", null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    categories = models.ManyToManyField(Category)
    isVideo = models.BooleanField(default=False)
    videoId = models.CharField(max_length=200, null = True, blank = True)
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

class Enquiry(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    studentCount = models.IntegerField()
    studentGender = models.CharField(max_length=30)
    tutorType = models.CharField(max_length=20)
    subject = models.CharField(default = "N.A", max_length=120)
    grade = models.CharField(default = "N.A", max_length=120)
    language = models.CharField(default = "N.A", max_length=120)
    level = models.CharField(default = "N.A", max_length=120)
    availableTime = models.TextField()
    learningStyle = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    note = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    arranged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "enquiries"


class Job(models.Model):
    title = models.CharField(max_length=150)
    salary = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    isClosed = models.BooleanField(default=False)

    def __str__(self):
        return self.title